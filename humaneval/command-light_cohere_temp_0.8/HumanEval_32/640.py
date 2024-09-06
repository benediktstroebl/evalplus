```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    Find polynomial zeros.
    xs = [1, x) + xs[1] * x + xs[2] * x**2 + ... + xs[-1] * x**(-1)  # Coefficients of polynomial
    n = len(xs)
    m = xs[-1]
    c = 1
    while True:
        z = 1 / (x**n - m * c)
        if z == 0:
            return [x for x in xs if x == z]
        c += 1
    return []

# Example usage
xs = [1, 2]
x = 0.1
result = poly(xs, x)
zeros = find_zero(xs)
assert len(zeros) == 1
assert result == zeros[0]
```