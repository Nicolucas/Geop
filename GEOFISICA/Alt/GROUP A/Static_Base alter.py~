# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=6>

# PARA LOS STATIC BASE

# <codecell>

#%pylab inline
from numpy import *
import numpy as np
import os
import pandas as pd
import urllib2
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt

os.getcwd()

# <codecell>

fileUrl=r'Static_Base.csv'
Data = read_csv(fileUrl,names=['data'])

# <markdowncell>

# Data['data']; data es el nombre de la lista de datos;
# si se coloca [num] muestra los datos de la fila [num].....

# <markdowncell>

# Por otro lado, si luego de colocar [num] se coloca [num][num2], num 2 va a ser el caracter dado

# <codecell>

print Data['data'][4]
print Data['data'][4][7:]

# <codecell>

print Data['data'][5]
print Data['data'][5][:2]
print Data['data'][5][2:4]
print type(int(Data['data'][5][4:6]))

# <markdowncell>

# El archivo Static_Base tiene dos columnas; UTC y TMI

# <codecell>

UTC=np.empty(0)
TMI=np.empty(0)
numdata=Data.index.shape[0]

# <codecell>

for i in range(numdata):
    seg=int(Data['data'][i][:2])*3600+int(Data['data'][i][2:4])*60+int(Data['data'][i][4:6])
    anomaly=double(Data['data'][i][7:])
    UTC=np.append(UTC,seg)
    TMI=np.append(TMI,anomaly)

# <codecell>


# <codecell>


