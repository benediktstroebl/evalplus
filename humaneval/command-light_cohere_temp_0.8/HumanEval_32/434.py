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
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    assert poly(1, x) == x - 0.5, "Error in find_zero"
    assert poly(2, x) == x**2 - 1, "Error in find_zero"
    assert poly(2, x - 1) == 0, "Error in find_zero"
    assert poly(3, x + 1) == x**3 + 2, "Error in find_zero"

Your script appears to evaluate polynomial, find zeros, and pass tests with the corresponding functions.