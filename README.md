# Retail-analysis-system

Machine Learning based Retail Analysis web application that performs customer segmentation using K-Means clustering, sales forecasting using Linear regression and data visualization using Matplotlib

## Project Overview

The Retail Analysis System is developed to analyze retail transaction data using machine learning algorithms. It processes raw data, identifies customer groups based on purchasing patterns, and predicts future sales values using historical sales information. The system helps in understanding customer behavior and supports data-driven decision-making.

## Features

- Data preprocessing and cleaning to prepare datasets for analysis.
- Customer segmentation using K-Means Clustering.
- Sales forecasting using Linear Regression.
- Data visualization through graphs for better understanding of results.
- Automated workflow from data loading to result generation.
- User-friendly interface for performing analysis.

## Technologies Used

### Programming Language
- Python

### Framework
- Flask

### Machine Learning Algorithms
- K-Means Clustering
- Linear Regression

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

### Frontend Technologies
- HTML

## System Workflow

1. Dataset is uploaded and loaded into the system.
2. Data preprocessing is performed to handle missing values, duplicates, and formatting.
3. Relevant features are selected for analysis.
4. K-Means Clustering is applied to segment customers.
5. Linear Regression is applied to forecast future sales.
6. Results are displayed using visualizations.

## Installation and Setup

Follow the steps below to run the Retail Analysis System on your local machine.

### 1. Clone the Repository

Download the project from GitHub by cloning the repository:

```bash
git clone https://github.com/Tanushree-U/Retail-analysis-system.git
```

### 2. Navigate to the Project Folder

Open the project directory:

```bash
cd Retail-analysis-system
```

### 3. Install Required Dependencies

Install all the required Python libraries using:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the Flask application:

```bash
python app.py
```

### 5. Access the Website

Open a web browser and enter:

```bash
http://127.0.0.1:5000⁠�
```

The Retail Analysis System will now be available on your local machine.

## Project Structure

```bash
Retail-analysis-system/
│
├── app.py
├── requirements.txt
├── templates/
├── static/
├── dataset/
└── README.md
```

## Results

### The system generates two major outputs:

#### Customer Segmentation: 
Groups customers into different segments based on their purchasing behavior using K-Means Clustering.

#### Sales Forecasting: 
Predicts future sales trends using Linear Regression based on historical sales data.

## Future Enhancements
* Integration with real-time retail databases and APIs.
* Implementation of advanced machine learning models.
* Development of a more interactive dashboard.
* Deployment on cloud platforms for public access.
* Support for multiple datasets and real-time analytics.

## Demo

The project is deployed and available at
```bash
https://retail-analysis-system.onrender.com
```

# Author
Tanushree U
