```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *x(i) * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial(x) = 0
    find_zero returns x with smallest absolute value
    """
    x = float('inf')
    for x in range(1, 100):
        p = poly(xs, x)
        if abs(p) < 1e-6:
            return x
    return float('inf')

xs = [1, 2]
x = find_zero(xs)
print("x is", x)
```