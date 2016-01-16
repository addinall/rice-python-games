import math

def a(s, l):
	return(0.25 * s * l ** 2 / math.tan(math.pi/s))


print a(5, 7)
print a(7, 3)

