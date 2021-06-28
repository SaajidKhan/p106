import csv
import numpy as np

def getDataSource(data_path):
    week=[]
    cofee_in_ml=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            week.append(float(row["week"]))
            cofee_in_ml.append(float(row["Coffee in ml"]))

        return{"x": week, "y": cofee_in_ml}

def findCorrelation(data_src):
    correlation=np.corrcoef(data_src["x"], data_src["y"])
    print("Correlation between Weeks and Coffee in ml :-    \n--->",correlation[0,1])

def setup():
    data_path="Cofee.csv"

    data_src=getDataSource(data_path)
    findCorrelation(data_src)

setup()


