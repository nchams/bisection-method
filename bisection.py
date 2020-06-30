import numpy as np

def f(x):
	return x**2 - 3

def bisection(a,b,tol):
	xl = a
	xr = b
	while (np.abs(xl-xr)>=0):
		c = (xl+xr)/2.0
		prod = f(xl)*f(c)
		if prod >tol:
			xl = c
		else:
			if prod<tol:
				xr = c
	return c

answer = bisection(-5,5,1e-4)
print("Bisection method gives root x = ", answer)