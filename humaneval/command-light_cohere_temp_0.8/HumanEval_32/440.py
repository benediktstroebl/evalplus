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
    It, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   , f(x) = x - sqrt(5)
    -0.3
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   , x = sqrt(5)
    -0.2
    >>> round(find_zero([1, -3, -10, -4, 2, -1, 1, -5, 4, -3, -1]), 2)
    -0.2

The script defines a function `poly` that evaluates a polynomial at a given point, and a function `find_zero` that finds the zero of a polynomial.

The `poly` function takes a list `xs` of coefficients and a point `x` as input, and returns the polynomial evaluation at the given point. The `find_zero` function takes a list `xs` of coefficients as input and finds the zero of the polynomial with those coefficients.

The `find_zero` function returns only the zero point of the polynomial, even if there are many roots. The function uses the approach of finding the largest non-zero coefficient and then solving the polynomial equation with this coefficient removed. This approach guarantees a have at most one solution, as polynomials with even number of coefficients have infinitely many roots.