def function(x):
	f = 6.9*x**0.64+2.152*x-2.152*46.6
	return f

def derivative(x):
	f1 = 6.9*0.64*x**(-0.36)+2.152
	return f1

def solve(x,iter=100,TOL=0.001):
	i = 0
	while i < iter:
		df = derivative(x)
		fx = function(x)
		x = x -fx/df
		t = abs(function(x)-0)
		i = i+1
		if t < TOL:
			break
			return x
			return i
	print(x)
	print(i)

solve(4.7)

