# JSON Cleaner for Large Datasets

## Overview
This project provides a Python script to clean large JSON files by removing empty fields, such as keys with empty strings (`""`), null values (`null`), or empty arrays (`[]`). This is particularly useful for datasets with many records, ensuring that the data remains structured and without unnecessary clutter.

## Features
- Handles large datasets efficiently (e.g., 18,000+ records).
- Recursively removes empty fields from JSON objects.
- Easy to use and customize for different types of JSON structures.
- Outputs a cleaned JSON file with the same structure but without empty fields.

## How to Use

### Step 1: Install Python
Ensure you have Python installed on your system. You can download the latest version from [here](https://www.python.org/downloads/).

### Step 2: Clone this Repository
```bash
git clone https://github.com/yourusername/JSON-Cleaner.git
cd JSON-Cleaner
