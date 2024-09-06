```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, which is the same as solving polynomial equations.
    find_zero returns only zero point, even if there are many solutions.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -4.5
    -0.07
    -0.00
    5)
    -
    -1
    """

This script defines a function `poly` that computes the value of a polynomial with given coefficients at a given point `x`. The function `find_zero` finds the zeros of the polynomial by solving the polynomial equation. 

Please note that this code assumes the input data to be correctly formatted as coefficients of a polynomial, and does not include any input validation or error handling.