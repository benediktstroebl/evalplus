```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes poly(x) = 0
    find_zero returns only zero point, even if there are many.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    1.
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    print(find_zero([5, 3, 5, -2])) # (-2) * (3 + 5) = -2 * 7
    -0.7
    ```
``` 
This code defines a function `poly` that computes the value of a polynomial with given coefficients at a given point `x`. It also defines a function `find_zero` that finds the zero of a polynomial `poly(x)` by evaluating it at `x = 0`. The function returns the value of `poly(x)` at `x = 0` which is the zero of the polynomial.