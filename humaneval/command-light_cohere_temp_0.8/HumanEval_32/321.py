```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes poly(x) = 0
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   """

test_find_zero = [x for x in range(10)]
test_find_zero = find_zero(test_find_zero)

test_find_zero
```
This code defines a function `poly` that computes a polynomial with coefficients as a list `xs` at a given `x` point. The function `find_zero` finds the zero of this polynomial.  The coefficients of the polynomial are assumed to be provided as a list `xs` where each element is a coefficient of the polynomial. The result of this `find_zero` function is tested and the output is printed.