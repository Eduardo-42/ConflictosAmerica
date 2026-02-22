import kagglehub
import os
import pandas as pd


def extractCSV(root):

    DATASETNAME= "mexwell/social-conflict-analysis-database"
    path = kagglehub.dataset_download(DATASETNAME)

    print("Path to dataset files:", path)
    csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]
    print("CSV Files:", csv_files)

    for file in csv_files:

        filepath = f"{path}/{file}"
        print(filepath)
        df = pd.read_csv(filepath, sep=",", encoding='mac_roman')
        
        toPath = f'{root}/{file}.csv'
        df.to_csv(toPath, index=False)


if __name__ == "__main__":
    extractCSV("./dataset")