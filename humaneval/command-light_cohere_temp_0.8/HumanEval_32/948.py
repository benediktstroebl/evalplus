```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**(n-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial (xs)(x) = 0
    find_zero returns only zero point, even if there are many solutions
    > round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x - 0.5
   
   
    print(f(x))
    """
    # largest non zero coefficient
    c = max(xs, key=lambda x: abs(x))
    # since coefficient is positive, x has to be negative
    x = -c
    # value of polynomial at x
    p = xs[0] + xs[1] * x + xs[2] * x**2 + ... + xs[-1] * x**(-n+1)
    return x, p
```