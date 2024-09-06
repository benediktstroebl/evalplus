```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes polynomial zero, returns only zero point, even if there are many.

    ensure that xs has even number of coefficients and largest non zero coefficient guarantees a solution.
    return math.floor(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0)
   1.0)
```
The above Python script defines a function `poly` that computes the polynomial for a list of coefficients and a point `x`. The function `find_zero` finds the zero of a polynomial, and passes the test that it only returns the zero for the function `poly`.