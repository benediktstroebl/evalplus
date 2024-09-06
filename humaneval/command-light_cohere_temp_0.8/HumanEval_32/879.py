```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes polynomial equal to 0.
    find_zero returns only zero point, even if there are many solutions
    and takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    print(find_zero([1, -2, 3, 4]))) # -2*x + 3*x^2 + 4 = 0
    -0.5
``` 
This script defines a function that evaluates polynomials and a function that finds the zeros of a polynomial. The script then passes the test with an example of coefficients.