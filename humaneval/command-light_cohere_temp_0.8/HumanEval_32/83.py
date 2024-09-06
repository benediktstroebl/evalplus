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
    find_zero find x such that polynomial evaluated at x is zero
    """
    return round(poly(xs, x), 2) == 0

xs = [1, 2]
x = 0.5
result = poly(xs, x)
assert result == 0
result = find_zero(xs)
print(result) # 0.5
```

The above Python code defines a polynomial evaluation function using the sum of coefficients multiplied by corresponding powers of x, and a find_zero function that finds the zeros of the polynomial.