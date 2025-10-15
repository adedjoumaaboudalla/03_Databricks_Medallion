
import json

# Chemin vers ton fichier config (dans ton repo Databricks ou DBFS)
config_path = "/Workspace/Users/joelledidanera@gmail.com/03_Databricks_Medallion/config/autoloader_config.json"


# Lecture du fichier
with open(config_path, "r") as f:
    config = json.load(f)

# Vérification du contenu
print(config)


source_schema = config["source_schema"]
source_path = config["source_path"]
bronze_path = config["bronze_path"]
bronze_checkpoint_path = config["bronze_checkpoint_path"]
silver_checkpoint_path = config["silver_checkpoint_path"]
gold_checkpoint_path = config["gold_checkpoint_path"]
file_format = config.get("file_format", "csv")