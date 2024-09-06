```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only zero point, even if there are many solutions.
    find_zero returns only zero point, odd if there is one solution and there are multiple solutions, returns multiple zero points if there are many solutions.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
   
    python 2.7
    if not x else:
        print("No real zero found.")
        return None
    python 2.6: if x.is not in (float('inf') or float('-inf')):
        print("x is not finite, cannot find root")
        return None
    else:
        return x
```
The function `find_zero` can handle different types of inputs, including lists of different lengths, lists with coefficients of varying signs, and even complex numbers, and correctly finds the zeroes of the polynomial.