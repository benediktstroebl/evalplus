```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n))

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial equal to zero, returns only zero point, and it ensures the list has even number of coefficients.

    if the polynomial has a list of coefficients and n is the order of polynomial, find_zero returns the list with n zeros, where n is the length of xs.
    }
   , largest non zero coefficient is guaranteed to be the first zero in the returned list.

>>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
-0.5
>>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
-0.3
``` 
This Python code defines two functions: `poly` evaluates a polynomial with coefficients `xs` at `x`, and `find_zero` finds the zero of a polynomial with coefficients `xs` using the `poly` function. The `find_zero` function returns only the zero point, ensuring the list of coefficients has an even number of coefficients.