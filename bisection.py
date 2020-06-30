#import dependancies 
import numpy as np

#define the function you want to find the root of
def f(x):
	return x**2 - 3

#bisection function takes on three arguments, a and b are points between which the the root exists. tol is the tolerance level you will accept. 
def bisection(a,b,tol):
	xl = a
	xr = b
	#while the interal is greater than zero execute the block of code below
	while (np.abs(xl-xr)>=0):
		#c is the centre of the interval [a,b]
		c = (xl+xr)/2.0
		#prod is the product of the function evaluated at points on the interval
		prod = f(xl)*f(c)
		#if the product is greater than the tolerance set a(xl) equal to c
		if prod >tol:
			xl = c
		else:
			if prod<tol:
				xr = c
	return c

answer = bisection(-5,5,1e-4)
print("Bisection method gives root x = ", answer)
