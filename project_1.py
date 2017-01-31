# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import argparse as arg
import numpy as np
import math
import matplotlib.pyplot as plt
import random

from project_1_fun import *
from vars_1 import *
            
#I'll begin with a system of size L

L = 16; #Change to get all the data

'''ARRAYS OF INTEREST:'''
z = [0]*L; #Array of slopes
zth = [0]*L; #Array of threshold slopes (chosen randomly for each site)
s = [0]; #SHOULDN'T BE AN ARRAY BUT CAN'T MAKE IT WORK OTHERWISE...Total height

t = 300000; #Added grains
AS = [0]*t; #Avalanche size after adding the grain
h = [0]*t; #Total height after the (t-1)'th added grain
AvSlope = [0]*t;#Average slope 

'''RANDOM CHOOSE A THRESHOLD SLOPE from zth for all i'''
for j in range (0,L):
    zth[j] = randz(p);

#Add a grain at the left-most site i=1 (s[0]) --> Drive. Lets do some iterations:
for j in range(0,t):

    AS[j] = Drive(s,z,zth);
    h[j] = s[0];
    AvSlope[j]=s[0]/L;

print("Total height after" , t, "added grains:", s)
print("Slopes of sites:", z)
print("Average slope after", t,"added grains:", AvSlope[t-1])

#Data saved to a text file

file_name = 'Total_height_' + str(L) + '.txt'

np.savetxt(file_name,h, fmt='%.18e', delimiter=' ', newline='\n', header='Total height:', footer='(function of t)', comments='# ')
