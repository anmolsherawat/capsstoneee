"""
ETL Pipeline - E-Commerce Analytics Capstone 2
Retail Sector | Customer Satisfaction & Revenue Analysis
"""

import pandas as pd
import numpy as np
import os

RAW_PATH = "data/raw/ecommerce_dataset.csv"
PROCESSED_PATH = "data/processed/ecommerce_cleaned.csv"

def extract(path):
    """Load raw dataset."""
    df = pd.read_csv(path)
    print(f"[EXTRACT] Loaded {df.shape[0]} rows, {df.shape[1]} cols")
    return df

def transform(df):
    """Clean and engineer features."""
    print(f"[TRANSFORM] Nulls before: {df.isnull().sum().sum()}")

    # Standardize city casing (e.g., 'pune' -> 'Pune')
    df['city'] = df['city'].str.strip().str.title()

    # Fill missing product_name
    df['product_name'] = df['product_name'].fillna('Unknown')

    # Fill missing payment_method
    df['payment_method'] = df['payment_method'].fillna('Unknown')

    # Fill missing delivery_days with median
    median_days = df['delivery_days'].median()
    df['delivery_days'] = df['delivery_days'].fillna(median_days)
    print(f"[TRANSFORM] Filled delivery_days nulls with median={median_days}")

    # Parse dates
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.month
    df['month_name'] = df['order_date'].dt.strftime('%B')
    df['week'] = df['order_date'].dt.isocalendar().week.astype(int)

    # Derived KPIs
    df['price_per_unit'] = (df['total_amount'] / df['quantity']).round(2)
    df['is_high_value'] = (df['total_amount'] >= df['total_amount'].quantile(0.9)).astype(int)
    df['fast_delivery'] = (df['delivery_days'] <= 3).astype(int)
    df['high_rating'] = (df['rating'] >= 4).astype(int)

    print(f"[TRANSFORM] Nulls after: {df.isnull().sum().sum()}")
    return df

def load(df, path):
    """Save cleaned dataset."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[LOAD] Saved {len(df)} rows to {path}")

def run():
    df = extract(RAW_PATH)
    df = transform(df)
    load(df, PROCESSED_PATH)
    print("[ETL COMPLETE]")
    return df

if __name__ == "__main__":
    run()
