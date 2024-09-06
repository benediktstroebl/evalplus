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
    find_zero find x that makes poly(x) = 0
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    return math.floor(math.sqrt(poly(xs[0]) / math.sqrt(xs[1]))
```
The script defines a function `poly` that evaluates a polynomial at a given point `x` by summing its coefficients `xs` with the `math.pow()` function. The function `find_zero` finds the zero of the polynomial `poly(x)` by searching for the value `x` that makes the polynomial equal to zero.