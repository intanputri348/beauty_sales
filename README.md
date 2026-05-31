# Beauty Marketplace Sales Analysis

## Overview

This project was created as part of a Data Analyst Technical Test for a Beauty & Cosmetic Marketplace business.

The objective of this analysis is to evaluate sales performance, marketplace effectiveness, product performance, customer behavior, and operational efficiency across multiple sales channels:

* TikTok Shop
* Shopee
* Official Website
* Offline Store

The project focuses not only on dashboard creation but also on generating actionable business insights and recommendations.

---

## Dataset Description

### 1. Product Master Table (`product_code`)

Contains detailed information about each beauty product.

**Primary Key**

* product_code

**Important Columns**

* product_name
* category
* shade
* production_cost
* selling_price
* stock_qty
* rating_average
* review_count

### 2. Sales Transaction Table (`transactions`)

Contains sales transactions from all sales channels.

**Primary Key**

* transaction_id

**Foreign Key**

* product_code

**Important Columns**

* transaction_date
* platform
* quantity
* gross_sales
* discount_amount
* net_sales
* platform_fee
* campaign_name
* delivery_status
* customer_rating
* returned_flag

---

## Data Model

A Star Schema model was implemented.

### Fact Table

* fact_sales_transactions

### Dimension Tables

* dim_products
* dim_calendar

Relationship:

dim_products.product_code
↓
fact_sales_transactions.product_code

Relationship Type:

* One-to-Many
* Single Direction Filter

---

## Data Cleaning Process

Data cleaning was performed using Python and Google Sheets.

### Cleaning Activities

#### Missing Values

* Checked all columns for null values.
* `return_reason` missing values were handled based on business logic.
* Missing return reasons for non-returned orders were labeled as "No Return".

#### Duplicate Check

* Verified transaction uniqueness using `transaction_id`.
* Removed duplicate records if found.

#### Data Type Validation

* Converted date fields into proper date format.
* Ensured numeric columns were stored correctly.

#### Business Validation

* Verified:

  * net_sales ≤ gross_sales
  * quantity > 0
  * production_cost > 0
  * stock_qty > 0

#### Feature Engineering

Created additional metrics:

* Profit
* Profit Margin
* Return Rate
* Age Group
* Campaign Performance
* Top Returned Product

---

## Dashboard Structure

### Page 1 — Executive Overview

Purpose:
Provide a high-level overview of business performance.

Contents:

* Total Sales
* Total Transactions
* Total Quantity Sold
* Total Profit
* Return Rate
* Sales Trend
* Sales by Platform
* Sales by Category

---

### Page 2 — Marketplace Performance

Purpose:
Evaluate channel effectiveness.

Contents:

* Profit Margin by Platform
* Top Payment Method
* Average Customer Rating
* Return Rate by Platform

---

### Page 3 — Product Performance

Purpose:
Analyze product contribution and inventory condition.

Contents:

* Top Best Selling Products
* Low Stock Alert
* Sales vs Profit
* Top Returned Products

---

### Page 4 — Customer & Operational Insight

Purpose:
Understand customer behavior and operational performance.

Contents:

* Customer Age Distribution
* Membership Tier Distribution
* Delivery Status Analysis
* Campaign Effectiveness
* Return Reason Analysis

---

## Key Business Insights

### Marketplace Insights

* Shopee generates the highest sales contribution.
* TikTok Shop produces strong revenue but requires monitoring of platform fees.
* Website and Offline Store show higher return rates.

### Product Insights

* Glow Matte Lip Cream is the best-selling product.
* Several products are approaching low stock levels.
* Skin Veil Foundation has the highest return volume.

### Customer Insights

* Customers aged 35+ contribute the highest number of transactions.
* Nearly half of customers belong to the Bronze membership tier.
* Customer ratings remain relatively similar across platforms.

### Operational Insights

* Wrong Shade is the most common return reason.
* Flash Sale campaign delivers the highest revenue.
* Current return rate is 5.4% and should be monitored.

---

## Recommendations

### Revenue Growth

* Strengthen Website sales contribution.
* Reduce dependency on Shopee.

### Customer Experience

* Improve shade recommendation system.
* Enhance customer service and product consultation.

### Inventory Management

* Prioritize restocking low-stock products.
* Implement reorder point monitoring.

### Customer Retention

* Improve loyalty programs.
* Encourage Bronze members to upgrade to higher tiers.

---

## Tools Used

### Data Cleaning

* Python
* Pandas
* Google Sheets

### Visualization

* Looker Studio

---

## Files Included

| File               | Description                           |
| ------------------ | ------------------------------------- |
| README.md          | Project documentation                 |
| cleaning.py        | Data cleaning script                  |
| insight_report.pdf | Business insights and recommendations |
| dashboard_link     | Looker Studio dashboard link          |

---

## Author

Intan Putri Mansyur Pratama
Beauty Marketplace Sales Analysis
Data Analyst Technical Test Submission
