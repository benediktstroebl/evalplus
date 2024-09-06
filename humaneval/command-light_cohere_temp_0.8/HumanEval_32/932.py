```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x, and also only returns x if there is exactly one solution, even if there are many solutions.
    >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    at x = -0.200003778526


xs = [1, -2, 3, -4, 5]
xs = [1, -2, 3, -4, 5]
xs = [1, -2, -3, -4, 5]
xs = [1, -2, 3, 4, 5]
xs = [1, -2, -3, 4, 5]
xs = [1, -2, 3, 4, 6]
xs = [1, -2, 3, 4, 7]
xs = [1, -2, 3, 4, 8]
xs = [1, -2, 3, 5, 4]
xs = [1, -2, 3, 4, 9]
xs = [1, -2, 3, 4, 10]
xs = [1, -2, 3, 5, 4]
xs = [1, -2, 3, 6, 4]
xs = [1, -2, 3, 7, 4]
xs = [1, -2, 4, 3, 5]
xs = [1, -3, 4, 5, 6]
xs = [1, -2, 3, 2, 4]
xs = [1, -2, 3, 2, 5]
xs = [1, -2, 3, 2, 6]
xs = [1, -2, 3, 2, 7]
xs = [1, -3, 4, 5, 6]
xs = [1, -2, 3, 2, 8]
xs = [1, -2, 3, 2, 9]
xs = [1, -2, 4, 5, 7]
xs = [1, -2, 3, 6, 7]
xs = [1, -2, 4, 5, 8]
xs = [1, -2, 3, 7, 8]
xs = [1, -2, 3, 8, 9]
xs = [1, -2, 4, 5, 9]
xs = [1, -2, 3, 6, 10]
xs = [1, -2, 3, 7, 10]
xs = [1, -2, 4, 5, 11]
xs = [1, -2, 3, 6, 12]
xs = [1, -2, 3, 7, 12]
xs =