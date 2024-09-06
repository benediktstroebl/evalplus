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
    find_zero find x such that poly(x) = 0,
        returns x, even if there are many solutions,
        returns None if there are no solutions
    """
    x = 0
    m = len(xs)
    while x < 0:
        if poly(xs, x) == 0:
            return x
        x += 1
    return None
``` 
The script defines a function `poly` that computes the polynomial expression with a list of coefficients and a point `x`. It then defines a function `find_zero` that finds the roots of the polynomial `poly(x)` = 0. It returns the `x` x- value that solves the polynomial equation, and returns `None` if there are no solutions.