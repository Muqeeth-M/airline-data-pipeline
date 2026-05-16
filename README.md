# ✈️ Airline Data Pipeline — Azure End-to-End Project

## Overview
An end-to-end data pipeline that ingests raw airline on-time performance data, 
applies transformation and cleaning logic using Python, and loads structured 
data into Azure SQL Database for reporting and analysis.

## Architecture
Raw CSV (Kaggle) → Azure Blob Storage → Azure Data Factory → Python Transformation → Azure SQL Database

## Tools & Technologies
- Azure Data Factory (ADF)
- Azure Blob Storage
- Azure SQL Database
- Python (Pandas)
- SQL / PL/SQL
- GitHub Actions

## Project Structure
airline-data-pipeline/
├── data/              # Cleaned dataset
├── Scripts/           # Python transformation scripts
├── sql/               # Azure SQL table creation scripts
├── adf_pipeline/      # ADF pipeline JSON exports
└── README.md

## Status
🚧 In Progress — actively being built
