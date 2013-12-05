import pylab
import numpy
import sys, string, os
from StringIO import StringIO

def convert(Filename,i):
    input=numpy.loadtxt(Filename)
    print input
    t=input
    c1=t[:,1]

    numData=shape(t)[0]
    c2=zeros(numData)
    for i in range(numData):
        c2[i]=(t[:2][i].replace(',','.'))
        print (c2[i])

   
