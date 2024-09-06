```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions
    """
    return math.floor(find(poly, x=xs[0]))


# Example usage:
xs = [1, 2]
x = 0.5
assert find_zero(xs) == 0.5


xs = [1, 2, -6, 11, -6, 1]
x = 0.0
assert find_zero(xs) == -1.0  # did not make x = 0.0, it's still an integer!  # Added test to make sure we're dealing with actual numbers, not floats.