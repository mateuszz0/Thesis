# PARAMETERS CELL ********************

Schema = "Spark DataFrame schema converted to JSON to enable passing it as a parameter"
SourceSystem = "Name of the source system"
SourceSchema = "Name of the schema of a table in the source (if applicable)"
SourceTable = "Name of the object in the source"
LoadMode = "0 for full-loaded tables, 1 for incrementally-loaded ones"
SourceKey = "PK of the table in the source system (if applicable)"
IncrementalPath = "Granular path for the recently ingested data, applicable only when LoadMode == 1"
FileFormat = "Format in which a data files are ingested"
SoftDeletes = "Flag indicating if soft deletes are enabled for a processed table"

# CELL ********************

DAG = {
    "activities": [
        {
            "name": "nb_BronzeLoader", 
            "path": "nb_BronzeLoader",
            "timeoutPerCellInSeconds": 3600,
            "args": {"Schema": Schema, "SourceSystem": SourceSystem, "SourceSchema": SourceSchema, "SourceTable":SourceTable, "LoadMode":LoadMode, "SourceKey":SourceKey, "FileFormat": FileFormat, "IncrementalPath": IncrementalPath}, 
        },
    ]
}

# CELL ********************

if SoftDeletes != '':
    notebookforkeys= {
        "name": "nb_BronzeLoaderForKeys",
        "path": "nb_BronzeLoaderForKeys",
        "timeoutPerCellInSeconds": 3600,
        "args": {"SourceSystem": SourceSystem, "SourceSchema": SourceSchema, "SourceTable":SourceTable, "LoadMode":LoadMode, "SourceKey":SourceKey, "FileFormat": FileFormat}, 
    }

    DAG['activities'].append(notebookforkeys)


# CELL ********************

combined_exec = mssparkutils.notebook.runMultiple(DAG, {"displayDAGViaGraphviz": False})

# CELL ********************

mssparkutils.notebook.exit(combined_exec['nb_BronzeLoader']['exitVal'])
