```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and finds zero coefficient polynomial
    no matter what values were provided, as long as xs has even number of coefficients.
    > round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    note that f(x) = -2x + 5x^2 + 6x^3 in this case.
    -0.5
    x value version of guaranteed to have one solution, not necessarily the simplest one.
    } 
```
This function can evaluate a polynomial given the coefficients and a point, and it can find a zero of the polynomial given the coefficients.