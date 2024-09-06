```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    """
    larger non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

```
The script defines two functions, poly and find_zero, to evaluate and find the zero of a polynomial, respectively. It uses the math library to calculate the polynomial coefficients and the power of a number.

The poly function takes a list of coefficients (xs) and a point (x) as input and returns the polynomial evaluated at the given point (x). The find_zero function takes a list of coefficients as input and returns the zero of the polynomial with those coefficients.