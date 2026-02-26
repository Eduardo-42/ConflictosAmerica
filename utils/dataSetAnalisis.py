import pandas as pd 
import os
import numpy as np

def showData(numOfRows,filepath):
    df = pd.read_csv(filepath, sep=",", encoding='mac_roman')
    tablewData= df.head(numOfRows)

    return tablewData


def showColumnNames(filepath):
    df = pd.read_csv(filepath, sep=",", encoding='mac_roman')
    columnArray= list(df.columns)

    return columnArray

def countryNames(filepath):
    df = pd.read_csv(filepath, sep=",", encoding='mac_roman')
    dafCountries = df.countryname.unique()

    return dafCountries



