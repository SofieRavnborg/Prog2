
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""


import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    inside_x =[]
    inside_y =[]
    outside_x =[]
    outside_y = []
    nc=0

    for i in range(0,n-1):
         x =r.uniform(-1, 1)
         y=r.uniform(-1,1)
         if x**2 + y**2<=1:
              inside_x.append(x)
              inside_y.append(y)
              nc+=1
         else:
              outside_x.append(x)
              outside_y.append(y)
    plt.figure(figsize=(8, 8))
    plt.scatter(inside_x, inside_y,color='blue')
    plt.scatter(outside_x, outside_y,color='red')
# Save the plot as a file
    plt.savefig(f'plot_with_{n}.png')  # Save before plt.show()

# Display the plot
    plt.show()
         
    
    # Write your code here
    return 4*nc/n
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
