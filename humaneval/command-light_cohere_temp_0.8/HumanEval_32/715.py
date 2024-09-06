```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    # Test polynomial by substituting in a list of values, 
    # first check if any list element makes it false.
    for x in range(0, 1, ...):
        if any(poly(xs, x) == 0):
            return x
    # Find largest non zero coefficient and return it
    for coeff in reversed(xs):
        if poly(xs, x) != 0 and xs[co] != 0:
            return xs[co]
    return 0  # return None if there are no solutions

# Test cases
xs = [1, 2]
x = [0.5, 1.0]
ans = find_zero(xs)
print("Solution:", end=" ", ans)

xs = [1, -2, 3]
x = [0.5, 1.0]
ans = find_zero(xs)
print("Solution:", end=" ", ans)

xs = [1, -2, -3]
x = [0.5, 1.0]
ans = find_zero(xs)
print("Solution:", end=" ", ans)
```
This Python script defines a function `poly` that evaluates a polynomial at a given point `x` using the given coefficients `xs`. The `find_zero` function takes a list of coefficients `xs` and finds the value of `x` that makes the polynomial equal to zero. 

Then, it tests the `poly` function by substituting a list of values, and checks if any list element makes the polynomial equal to zero. Finally, it finds the largest non zero coefficient in `xs` and returns it, or returns `None` if there are no solutions. 

This script can be used to evaluate polynomial functions and find the values of `x` that make the polynomial equal to zero, which can be useful in various mathematical and computational tasks.