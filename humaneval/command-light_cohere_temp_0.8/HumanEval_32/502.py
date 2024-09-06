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
    find_zero find x such that polynomial(x) = 0.
    find_zero returns only zero point, even if there are many
    solutions.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    ```

This script defines a function `poly` that computes the value of a polynomial with given coefficients at a given point `x`. It also defines a function `find_zero` that finds the zero of a polynomial with given coefficients. The `find_zero` function returns the zero of the polynomial only if the list of coefficients `xs` has an even number of coefficients and the largest coefficient is non-zero.