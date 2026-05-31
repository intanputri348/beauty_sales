# Beauty Marketplace Sales Analysis

## Deskripsi Proyek

Proyek ini dibuat sebagai bagian dari Technical Test Data Analyst untuk perusahaan Beauty & Cosmetic Marketplace.

Tujuan analisis adalah mengevaluasi performa penjualan, efektivitas marketplace, performa produk, perilaku pelanggan, dan efisiensi operasional berdasarkan data transaksi dari berbagai channel penjualan, yaitu:

* Shopee
* TikTok Shop
* Website Resmi
* Offline Store

Fokus utama proyek ini tidak hanya pada visualisasi dashboard, tetapi juga menghasilkan insight bisnis yang dapat digunakan sebagai dasar pengambilan keputusan.

---

## Dataset

### 1. Tabel Product Master (`product_code`)

Berisi informasi detail setiap produk.

**Primary Key**

* product_code

**Kolom Penting**

* product_name
* category
* shade
* production_cost
* selling_price
* stock_qty
* rating_average
* review_count

### 2. Tabel Transactions (`transactions`)

Berisi seluruh transaksi penjualan dari berbagai channel.

**Primary Key**

* transaction_id

**Foreign Key**

* product_code

**Kolom Penting**

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

## Data Modeling

Model data yang digunakan adalah **Star Schema**.

### Fact Table

* fact_sales_transactions

### Dimension Table

* dim_products
* dim_calendar

Relationship:

dim_products.product_code

↓

fact_sales_transactions.product_code

Tipe Relationship:

* One-to-Many
* Single Direction Filter

---

## Proses Data Cleaning

Proses data cleaning dilakukan menggunakan Python dan Google Sheets.

### Tahapan Cleaning

#### 1. Pemeriksaan Missing Values

* Mengecek seluruh kolom yang memiliki nilai kosong.
* Menangani missing value pada kolom `return_reason`.
* Mengisi transaksi yang tidak diretur dengan nilai "No Return".

#### 2. Pemeriksaan Duplikasi

* Memastikan tidak terdapat duplikasi pada `transaction_id`.

#### 3. Validasi Tipe Data

* Mengubah kolom tanggal menjadi format date.
* Memastikan kolom numerik tersimpan dalam format yang sesuai.

#### 4. Validasi Data Bisnis

Melakukan pengecekan:

* quantity > 0
* net_sales ≤ gross_sales
* production_cost > 0
* stock_qty > 0

#### 5. Feature Engineering

Membuat kolom dan metrik tambahan untuk mendukung analisis bisnis:

Kolom Tambahan:
- Year
- Quarter
- Month
- Month Name
- Day Name
- Age Group

Metrik Tambahan:
- Profit
- Profit Margin
- Return Rate
- Returned Transaction

---

## Struktur Dashboard

### Halaman 1 – Executive Overview

Tujuan:
Memberikan gambaran umum performa bisnis.

Visualisasi:

* Total Sales
* Total Transaksi
* Total Quantity Sold
* Total Profit
* Return Rate
* Sales Trend
* Sales by Platform
* Sales by Category

---

### Halaman 2 – Marketplace Performance

Tujuan:
Mengevaluasi performa masing-masing channel penjualan.

Visualisasi:

* Profit Margin by Platform
* Top Payment Method
* Average Customer Rating
* Return Rate by Platform

---

### Halaman 3 – Product Performance

Tujuan:
Menganalisis kontribusi produk terhadap bisnis.

Visualisasi:

* Top Best Selling Products
* Low Stock Alert
* Sales vs Profit
* Top Returned Products

---

### Halaman 4 – Customer & Operational Insight

Tujuan:
Memahami karakteristik pelanggan dan efisiensi operasional.

Visualisasi:

* Customer Age Distribution
* Membership Tier Distribution
* Delivery Status Analysis
* Campaign Effectiveness
* Return Reason Analysis

---

## Insight Utama

### Marketplace

* Shopee menjadi channel dengan kontribusi penjualan terbesar.
* TikTok Shop menghasilkan penjualan tinggi namun perlu memperhatikan biaya platform.
* Website dan Offline Store memiliki tingkat retur yang relatif lebih tinggi.

### Produk

* Glow Matte Lip Cream menjadi produk terlaris.
* Beberapa produk memiliki stok rendah dan berisiko mengalami stockout.
* Skin Veil Foundation menjadi produk yang paling sering diretur.

### Pelanggan

* Kelompok usia 35+ merupakan segmen pelanggan terbesar.
* Hampir 50% pelanggan berada pada tier Bronze.
* Rata-rata rating pelanggan masih berada pada kisaran 3 dari 5.

### Operasional

* Wrong Shade menjadi alasan retur terbesar.
* Flash Sale merupakan campaign dengan performa terbaik.
* Return Rate saat ini berada di angka 5,4%.

---

## Rekomendasi Bisnis

### Peningkatan Penjualan

* Meningkatkan kontribusi penjualan melalui Website.
* Mengurangi ketergantungan terhadap satu marketplace.

### Pengalaman Pelanggan

* Menambahkan fitur rekomendasi shade.
* Meningkatkan kualitas customer service.

### Manajemen Persediaan

* Memprioritaskan restock produk dengan stok rendah.
* Menerapkan sistem reorder point.

### Loyalitas Pelanggan

* Mengembangkan program loyalty.
* Mendorong pelanggan Bronze naik ke Silver dan Gold.

---

## Tools yang Digunakan

### Data Cleaning

* Python
* Pandas
* Google Sheets

### Visualisasi

* Looker Studio

### Dokumentasi

* Markdown

---

## Struktur Proyek

```text
.
├── cleaning.py          # Script Python untuk pembersihan dan pra-pemrosesan data
├── dashboard_link       # File teks atau dokumen berisi tautan dashboard interaktif
├── insight_report.pdf   # Laporan analisis bisnis lengkap dalam format PDF
└── README.md            # Dokumentasi utama proyek

Author
Intan Mahasiswa Informatika
Technical Test – Beauty Marketplace Sales Analysis
