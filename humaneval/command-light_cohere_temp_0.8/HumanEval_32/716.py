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
    find_zero find x such that poly(x) = 0
    find_zero returns x, which satisfies x - a = b0 and x - b1 = b2 for some a, b in xs.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
    """ f(x) = 2x + 5x^2 - 3x^3 - 6x^4 + x^5
    -0.7
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -0.9
    """ -
    4
```