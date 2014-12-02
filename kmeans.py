from numpy import *
import scipy as sp
from pandas import *
from rpy2.robjects.packages import importr
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
import pandas.rpy.common as com
import pandas as pd
from pandas import DataFrame


with open("Data\cars.csv", 'r') as csv_file:
    pandas2ri.activate()
    dataframe = read_csv(csv_file)
    r_dataframe = com.convert_to_r_dataframe(dataframe)
    klaR = importr("klaR")
    KMC = klaR.kmodes(r_dataframe, 5)
    dataframe['clusterID'] = KMC[0]
    print(dataframe)























