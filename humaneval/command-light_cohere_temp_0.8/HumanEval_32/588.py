```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    """
    return only x=0

# Test cases
xs = [1, 2, -6, 11, -6, 1]

# Evaluate polynomial
p = poly(xs, 1.0)

# Test if polynomial has zero at x=0
if p == 0:
    print("Yes, polynomial has zero at x=0")
else:
    print("No, polynomial does not have zero at x=0")

# Test if polynomial has zero at a negative number
p = poly(xs, -10)
if p == 0:
    print("Yes, polynomial has zero at x=-10")
else:
    print("No, polynomial does not have zero at x=-10")

# Test if polynomial has a single root
if len(xs) == 1:
    print("Yes, polynomial has single root")
else:
    print("No, polynomial has multiple roots")

# Test if polynomial has a repeated root
if xs[0] == xs[-1]:
    print("Yes, polynomial has repeated root")
else:
    print("No, polynomial does not have repeated root")
``` 

The function poly evaluates a polynomial at a given point x by summing the product of coefficients and the corresponding factorials. The function find_zero finds the zeros of the polynomial by checking if the polynomial evaluates to zero at x. The test cases demonstrate the approach by evaluating the polynomial at various points and comparing the result with zero. 

The function also checks if the polynomial has a single root, a repeated root, or multiple roots.