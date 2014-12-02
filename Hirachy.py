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
    distances = ro.r.dist(r_dataframe, method="euclidean") #specify the distance
    clusterinput = ro.r.hclust(distances, method="ward.D")
    clusterGroups = ro.r.cutree(clusterinput, k=5) #specify the number of clusters
    dataframe['clusterID'] = clusterGroups
    print(dataframe)









