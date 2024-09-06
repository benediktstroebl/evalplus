```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that polynomial(x) = 0, returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x - 0.5
   
   
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -1.0
   
    fact that there is only one solution.
    """

The script defines two functions, `poly` and `find_zero`, that evaluate a polynomial and find its zeros, respectively. The `poly` function takes a list of coefficients `xs` and a point `x` as input, and returns the polynomial's evaluation at `x`. The `find_zero` function takes a list of coefficients `xs` as input, and finds the zero of the polynomial at `x`.