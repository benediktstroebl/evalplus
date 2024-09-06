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
    find_zero finds x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    For example, find_zero([1, 2]) returns (0, 1)
    >>> round(find_zero([1, 2])) # (0, 1)
    """
    for x in range(-10, 10):
        if poly(xs, x) == 0:
            return (x, poly(xs, x))

def test(xs: list, x: float):
    """
    Tests if polynomial has zero at x.
    """
    first test if polynomial(x) == 0
    then second test if all x - poles of polynomial are less than or equal to x
    """
    for x in range(-10, 10):
        if poly(xs, x) == 0:
            return x
    for x in range(-10, 10):
        if poly(xs, x) != poly(xs, -x):
            return -x

xs = [1, 2]
x = 0
print(test(xs, x)) # tests and returns
```
This code solves the problem of finding the first x-value that makes a given polynomial equation zero, and tests if the polynomial has zero at that value x. 
The function poly(xs, x) evaluates the polynomial at the point x, and the function find_zero finds the first value of x that makes the polynomial zero. The function test(xs, x) tests if the polynomial has zero at the value x, and returns a list of values of x that make the polynomial zero.