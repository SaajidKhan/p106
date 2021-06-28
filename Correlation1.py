import csv
import numpy as np

def getDataSource(data_path):
    marks_in_percentage=[]
    days_present=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

        return{"x": marks_in_percentage, "y": days_present}

def findCorrelation(data_src):
    correlation=np.corrcoef(data_src["x"], data_src["y"])
    print("Correlation between Marks in Percentage and Days Present :-   \n--->",correlation[0,1])

def setup():
    data_path="Student.csv"

    data_src=getDataSource(data_path)
    findCorrelation(data_src)


setup()


