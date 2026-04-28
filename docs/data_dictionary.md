# Data Dictionary

## Source Dataset: ecommerce_dataset.csv

| Column | Type | Description | Example | Notes |
|--------|------|-------------|---------|-------|
| order_id | int | Unique order identifier | 1000 | Range: 1000–10999 |
| customer_id | str | Customer identifier | C960 | Format: C + 3 digits |
| order_date | date | Date of order placement | 2024-01-15 | Range: Jan–Mar 2024 |
| product_category | str | Category of product | Electronics | 4 categories |
| product_name | str | Product name | Jacket | 500 nulls (filled: 'Unknown') |
| price | int | Unit price in INR | 56622 | Range: ₹209–₹299,980 |
| quantity | int | Units ordered | 4 | Range: 1–5 |
| total_amount | int | price × quantity | 226488 | Derived field |
| payment_method | str | Payment type used | COD | Card/COD/UPI; 500 nulls |
| city | str | Delivery city | Mumbai | 5 cities; 'pune' normalised to 'Pune' |
| delivery_days | float | Days to deliver | 8.0 | 500 nulls; filled with median (5.0) |
| rating | int | Customer rating 1–5 | 5 | No nulls |

## Engineered Columns (in processed dataset)

| Column | Description |
|--------|-------------|
| month | Order month number (1–3) |
| month_name | Order month name (January–March) |
| week | ISO week number |
| price_per_unit | total_amount / quantity |
| is_high_value | 1 if total_amount >= 90th percentile |
| fast_delivery | 1 if delivery_days <= 3 |
| high_rating | 1 if rating >= 4 |

## Product Categories
- **Clothing** — Jackets, T-shirts, Jeans, Sarees, Kurtas
- **Electronics** — Headphones, Laptops, Mobiles, Cameras, TVs
- **Furniture** — Sofas, Beds, Chairs, Tables, Wardrobes
- **Groceries** — Oils, Spices, Pulses, Rice, Atta

## Cities
- Mumbai, Delhi, Bangalore, Chennai, Pune
