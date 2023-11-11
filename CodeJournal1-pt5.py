#import module(s)
import numpy as np 
from astropy.table import table 
from astropy.io import ascii
from astropy.io import fits 

#add a data array
x = np.linspace(0,2*pi,1000);
y = sin(x),x

#create a table
data = Table([x,y],names=["sin(x),x"])

#write the table to file
ascii.write(data, 'table.txt', format= 'commented_header')

#read data, print table
data_in = ascii.read('table.txt')
print(data_in)