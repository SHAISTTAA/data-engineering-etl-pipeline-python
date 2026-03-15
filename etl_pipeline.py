
import pandas as pd
import sqlite3
from datetime import datetime

# -----------------------------
# Extract Step
# -----------------------------
def extract_data(file_path):
    print("Extracting data from CSV...")
    df = pd.read_csv(file_path)
    print(f"Loaded {len(df)} records")
    return df


# -----------------------------
# Transform Step
# -----------------------------
def transform_data(df):
    print("Transforming data...")

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Calculate total order value
    df["total_value"] = df["price"] * df["quantity"]

    # Add tax calculation (18%)
    df["tax"] = df["total_value"] * 0.18

    # Final price after tax
    df["final_amount"] = df["total_value"] + df["tax"]

    # Normalize product names
    df["product"] = df["product"].str.lower()

    # Add processing timestamp
    df["processed_at"] = datetime.now()

    return df


# -----------------------------
# Analytics Transformation
# -----------------------------
def generate_summary(df):
    print("Generating summary metrics...")

    summary = df.groupby("category").agg(
        total_orders=("order_id", "count"),
        total_revenue=("final_amount", "sum"),
        avg_order_value=("final_amount", "mean")
    ).reset_index()

    return summary


# -----------------------------
# Load Step
# -----------------------------
def load_data(df, summary_df, db_name="sales_data.db"):
    print("Loading data into database...")

    conn = sqlite3.connect(db_name)

    df.to_sql("sales_transactions", conn, if_exists="replace", index=False)
    summary_df.to_sql("sales_summary", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print("Data successfully stored in database.")


# -----------------------------
# Pipeline Execution
# -----------------------------
def run_pipeline():
    data_path = "data/sales_data.csv"

    raw_data = extract_data(data_path)

    transformed_data = transform_data(raw_data)

    summary = generate_summary(transformed_data)

    load_data(transformed_data, summary)

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
