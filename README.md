# 🚗 Databricks Lakehouse - Vehicle Sales Pipeline  🚧🚧🚧

## 📘 Description  
Ce projet illustre la mise en place d’une architecture **Delta Lake (Bronze / Silver / Gold)** sur **Databricks**, appliquée au domaine automobile.  
L’objectif est de simuler une chaîne analytique complète de ventes de véhicules, depuis l’ingestion automatique des fichiers bruts jusqu’à la génération de tables d’analyse prêtes à la consommation par les outils BI.

L’ingestion des données se fait en **streaming via Auto Loader** depuis un répertoire Cloud Storage (Azure Data Lake, AWS S3 ou GCS).


## 🏗️ Architecture

### 🥉 Bronze Layer
- **Source** : fichiers bruts (CSV, JSON, Parquet) stockés dans le cloud.
- **Ingestion** : via **Auto Loader** (`cloudFiles`) en mode streaming.  
- **Objectif** : stocker les données brutes telles qu’elles sont reçues.

### 🥈 Silver Layer
- Nettoyage, normalisation et enrichissement :
  - Suppression des doublons et des valeurs nulles.
  - Conversion des types de données.
  - Jointures entre tables : `vehicles`, `customers`, `sales`.
- Utilisation du **Change Data Feed (CDF)** pour la capture des changements.

### 🥇 Gold Layer
- Tables analytiques prêtes pour Power BI / Tableau :
  - `country_sales_stats` : ventes par pays.
  - `vehicle_brand_stats` : statistiques par marque.
  - `sales_rep_performance` : performance des vendeurs.


## 📂 Structure du dépôt
  - config : Les fichiers de configuration comme les path fixe
  - includes : Les fichier de join par exemple
  - notebooks : Les notes book pour la création du pipeline



## ⚙️ Technologies utilisées
- **Databricks Runtime 13.3+**
- **Delta Lake**
- **Auto Loader** (`cloudFiles`)
- **Spark Structured Streaming**
- **Change Data Feed (CDF)**
- **Python (PySpark)**


## 1️⃣ Configuration du Cloud Storage
Définir les chemins sources et cibles dans `configs/autoloader_config.json` :
```json
{
  "source_schema": "source_type STRING, value STRING",
  "source_path": "gs://vehicle_sales_data/raw/",
  "bronze_path": "dbfs:/mnt/bronze/",
  "silver_path": "dbfs:/mnt/silver/",
  "gold_path": "dbfs:/mnt/gold/",
  "bronze_checkpoint_path": "dbfs:/mnt/bronze/checkpoint",
  "silver_checkpoint_path": "dbfs:/mnt/silver/checkpoint",
  "gold_checkpoint_path": "dbfs:/mnt/gold/checkpoint"
}

