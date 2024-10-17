
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
import numpy as np
import functools

def sphere_volume(n, d):
    dist = [functools.reduce(lambda x,y : x+y,[r.uniform(-1, 1)**2 for jj in range(0,d)]) for ii in range(0,n)]
    list_nc = list(filter(lambda x: x<=1,dist))

    nc = len(list_nc)

    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 

    return (nc/n)*(2**d)

def hypersphere_exact(n,d):
    return ((m.pi)**(d/2))/(m.gamma(d/2+1))
     
def main():
    n = 100000
    d = 2
    sphere_volume(n,d)


if __name__ == '__main__':
	main()
