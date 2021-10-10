import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Marks In Percentage", y = "Days Present")
        fig.show()

def getDataSource(data_path):
    marks = []
    attendance = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            attendance.append(float(row["Days Present"]))
    return{"x": marks, "y" : attendance}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between days present and marks in percentage is", correlation[0, 1])

def setup():
    data_path = "marks.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()

