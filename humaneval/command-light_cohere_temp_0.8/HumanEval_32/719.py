```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and finds the maximum non zero coefficient.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """ >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
    finding a simple zeros of the polynomial, it does not guarantee any particular structure of the solutions.

This function implements the Zeros theorem which states that if P(x) is a polynomial of degree n with integer coefficients, then there are exactly n zeros in the interval (-infinity, 1).

The function also finds the largest non-zero coefficient, which is needed to guarantee that there is always a solution in the interval. 

This function runs in O(n) time where n is the number of coefficients in the polynomial, and has a time complexity of O(1) since it only needs to iterate over the list once.