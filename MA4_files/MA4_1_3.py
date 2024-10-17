
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
import functools
import concurrent.futures

def sphere_volume(n, d):
    dist = [functools.reduce(lambda x,y : x+y,[r.uniform(-1, 1)**2 for jj in range(0,d)]) for ii in range(0,n)]
    list_nc = list(filter(lambda x: x<=1,dist))

    nc = len(list_nc)

    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 

    return (nc/n)*(2**d)

def hypersphere_exact(n,d):
    return ((m.pi)**(d/2))/(m.gamma(d/2+1))

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(np):
             futures.append(executor.submit(sphere_volume,n,d))
        results = [f.result() for f in futures]
    total_volume = sum(results) / np
     #using multiprocessor to perform 10 iterations of volume function  
    return total_volume

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    sub_n = n//np
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(np):
             futures.append(executor.submit(sphere_volume,sub_n,d))
        results = [f.result() for f in futures]
    total_volume = sum(results) / np
     #using multiprocessor to perform 10 iterations of volume function  
    return total_volume

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11

    for y in range (10):
        sphere_volume(n,d)


if __name__ == '__main__':
	main()
