from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

df_global = None

# -----------------------------
# 1. UPLOAD PAGE
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def upload():
    global df_global

    if request.method == "POST":
        file = request.files["file"]
        df_global = pd.read_csv(file).drop_duplicates()

        # Date detection (any column containing "date")
        date_col = None
        for col in df_global.columns:
            if "date" in col.lower():
                date_col = col
                break

        if date_col:
            df_global["Date"] = pd.to_datetime(df_global[date_col], errors="coerce")
        else:
            df_global["Date"] = None

        columns = list(df_global.select_dtypes(include='number').columns)

        return render_template("select.html", columns=columns)

    return render_template("upload.html")


# -----------------------------
# 2. COLUMN SELECTION AND ANALYSIS
# -----------------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    global df_global

    xcol = request.form["xcol"]
    ycol = request.form["ycol"]

    data = df_global[[xcol, ycol]].dropna()

    # Scaling
    scaler = StandardScaler()
    scaled = scaler.fit_transform(data)

    # Clustering
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    data["Cluster"] = kmeans.fit_predict(scaled)

    counts = data["Cluster"].value_counts().to_dict()

    # Cluster insights
    cluster_means = data.groupby("Cluster")[[xcol, ycol]].mean()
    cluster_means["Business Score"] = (
        cluster_means[xcol] * 0.7 + cluster_means[ycol] * 0.3
    )

    sorted_clusters = cluster_means.sort_values(by="Business Score")

    labels = ["Low-value", "Medium", "High-value"]

    interpretation = []
    for i, cluster in enumerate(sorted_clusters.index):
        interpretation.append({
            "cluster": int(cluster),
            "label": labels[i],
            "x": round(cluster_means.loc[cluster, xcol], 2),
            "y": round(cluster_means.loc[cluster, ycol], 2)
        })

    # -----------------------------
    # 3. CLUSTER GRAPH
    # -----------------------------
    plt.figure()
    plt.scatter(data[xcol], data[ycol], c=data["Cluster"])
    plt.xlabel(xcol)
    plt.ylabel(ycol)
    plt.title("Clustering")
    plt.savefig("static/cluster.png")
    plt.close()

    # -----------------------------
    # 4. FORECAST (ONLY IF DATE EXISTS)
    # -----------------------------
    forecast = None

    if "Date" in df_global.columns and df_global["Date"] is not None and df_global["Date"].notna().any():

        try:
            if "Total Amount" in df_global.columns:

                daily_sales = df_global.groupby("Date")["Total Amount"].sum().reset_index()
                daily_sales["Date_Num"] = daily_sales["Date"].map(pd.Timestamp.toordinal)

                X = daily_sales[["Date_Num"]]
                y = daily_sales["Total Amount"]

                model = LinearRegression()
                model.fit(X, y)

                last_date = daily_sales["Date"].max()
                future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, 8)]

                future_X = pd.DataFrame({
                    "Date_Num": [d.toordinal() for d in future_dates]
                })

                predictions = model.predict(future_X)

                forecast = []
                for d, val in zip(future_dates, predictions):
                    forecast.append({
                        "date": str(d.date()),
                        "value": round(val, 2)
                    })

                # Forecast graph
                plt.figure()
                plt.plot(daily_sales["Date"], y, label="Actual")
                plt.plot(future_dates, predictions, linestyle="dashed", label="Forecast")
                plt.legend()
                plt.title("Forecast")
                plt.savefig("static/forecast.png")
                plt.close()

            else:
                forecast = "NO_AMOUNT"

        except:
            forecast = "NOT_AVAILABLE"

    else:
        forecast = "NOT_AVAILABLE"

    # -----------------------------
    # 5. RESULT PAGE
    # -----------------------------
    return render_template("result.html",
                           counts=counts,
                           interpretation=interpretation,
                           forecast=forecast)

@app.route("/shutdown", methods=["POST"])
def shutdown():
    os._exit(0)

if __name__ == "__main__":
    app.run(debug=True)