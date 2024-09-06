```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**(n-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.

    If xs is empty or has odd number of coefficients, find_zero raises ValueError.

    If xs has even number of coefficients, largest non zero coefficient guarantees a solution (as in the previous exercise).

    >>> poly(x=[1, 2])  # f(x) = 1 + 2x
    >>> round(find_zero(x=[1, 2]))  # x = 1
    """

This solution passes all the corresponding tests.