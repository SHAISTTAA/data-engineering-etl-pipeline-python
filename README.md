# Data Engineering Sales ETL Pipeline

This project demonstrates a simple data engineering pipeline built using Python.

The pipeline extracts sales data from a CSV file, performs several transformations, and loads the processed data into a SQLite database.

## Features

- CSV data ingestion
- Data transformation using Pandas
- Revenue and tax calculations
- Aggregated sales analytics
- Database storage

## Technologies

Python  
Pandas  
SQLite  
SQLAlchemy

## ETL Workflow

1. Extract sales data from CSV
2. Transform the dataset
   - normalize product names
   - compute order totals
   - calculate tax
3. Generate category level analytics
4. Load processed data into database tables

## Run the Project

Install dependencies

pip install -r requirements.txt

Run pipeline

python etl_pipeline.py

## Output

Database file created:

sales_data.db

Tables inside database:

sales_transactions  
sales_summary
