```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.append(x polynomial=sum(xs)
    return polynomial

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that polynomial(x)=0
    find_zero returns x that satisfies this condition
    """
    polynomial = poly(xs, x)
    return math.floor(polynomial)
```