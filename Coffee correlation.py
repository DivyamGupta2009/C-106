import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x" : coffee, "y" : sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between coffee in ml and sleep hours is", correlation[0,1])

def setup():
    data_path = "coffee.csv"
    data_source  = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()
    
