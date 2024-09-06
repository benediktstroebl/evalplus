```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *pow(i, x) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns x
    """
    return math.floor(solve(poly(xs, x=find_zero)))

def solve(xs: list):
    """
    Test case 1:
    >>> solve([1, 2])
    1.0
    Test case 2:
    >>> solve([-6, 11, -6, 1])
    -1.0
    Test case 3:
    >>> solve([1, -1, 1, 2])
    0.0
    Test case 4:
    >>> solve([1, 2, 2, 2])
    1.0
    Test case 5:
    >>> solve([1, -3, -1, -2, 2])
    -1.0
    Test case 6:
    >>> solve([-2, -1, 1, 2, 3])
    0.0
    Test case 7:
    >>> solve([1, 1, 2, 1, 3])
    1.0
    Test case 8:
    >>> solve([1, -1, -2, 1, 3])
    -0.1
    Test case 9:
    >>> solve([1, -4, -3, -2, 3])
    -0.2
    Test case 10:
    >>> solve([-3, -2, -1, 2, 3])
    0.0
    Test case 11:
    >>> solve([-6, 11, -6, 1])
    -1.0
    Test case 12:
    >>> solve([1, -5, -4, -3, 2])
    -0.5
    Test case 13:
    >>> solve([1, 2, 3, 1, 4])
    2.0
    Test case 14:
    >>> solve([1, -3, -5, -6, 2])
    -0.0
    Test case 15:
    >>> solve([1, -1, -4, -5, 2])
    -0.0
    Test case 16:
    >>> solve([-1, -2, -3, -5, 2])
    -0.0
    Test case 17:
    >>> solve([1, -6, -5, -4, 2])
    0.0
    Test case 18:
    >>> solve([1, -7, -6, -5, 2])
    -0.0
    Test case 19:
    >>> solve([1, -8, -7, -6, 2])
    0.0
    Test case 20:
    >>> solve([1, -9, -8, -7, 2])
    0.0
    Test case 21:
    >>> solve([1, -10, -9, -8, 2])
    0.0
    Test case 22:
    >>> solve([1, -11, -10, -9, 2])
    0.0
    Test case 23:
    >>> solve([1, -12, -11, -10, 2])
    0.0
    Test case 24:
    >>> solve([1, -13, -12, -11, 2])
    0.0
    Test case 25:
    >>> solve([1, -14, -13, -12, 2])
    0.0
    Test case 26:
    >>> solve([1, -15