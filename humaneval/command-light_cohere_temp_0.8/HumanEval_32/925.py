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
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.

    If list xs have an coefficient that is non zero, then there will be no solution.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
   
   
    ^1
    -0.05
    > 1
       
    -5
    -0.5
    <
   
    -1
```

This Python script defines a self-contained function `poly` that evaluates a polynomial with given coefficients at a given point `x`. The function returns the result of the polynomial evaluation. The function `find_zero` finds the zero of a polynomial with given coefficients. It returns only the values that satisfy the polynomial equation.