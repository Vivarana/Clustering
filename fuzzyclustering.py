from numpy import *
import scipy as sp
from pandas import *
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
import pandas.rpy.common as com
from pandas import DataFrame


with open("Data\cars.csv", 'r') as csv_file:
    dataframe = read_csv(csv_file)
    r_dataframe = com.convert_to_r_dataframe(dataframe)
    cluster  = importr("cluster")
    cfuz = cluster.fanny(r_dataframe,3)
    dataframe['clusterID'] = cfuz[3]
    print(dataframe)

