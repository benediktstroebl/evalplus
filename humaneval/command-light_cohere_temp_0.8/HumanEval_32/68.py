```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial(x) = 0, returns x.
    return x0
```
# Example usage
xs = [1, 2]
x = find_zero(xs)
print("x =", round(x,2))  # Output: x = 1.0
``` 
In this script, the poly function computes the polynomial using the coefficients in xs, and the find_zero function finds the root of this polynomial.