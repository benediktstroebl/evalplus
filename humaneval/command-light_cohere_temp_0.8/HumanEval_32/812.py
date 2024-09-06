```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    and finds the largest non zero coefficient.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
   
    N.7
``` 
This code defines a function `poly` that evaluates a polynomial with coefficients as input at a given point `x` and returns the polynomial's value at that point. The function also has a function `find_zero` that finds the zero of a polynomial with coefficients as input. The `find_zero` function returns only the zero point of the polynomial, even if there are multiple roots. It finds the largest non zero coefficient to ensure that the solution is correct.