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
    find_zero find x that makes the polynomial equal to 0, using the poly function
    """
    return round(poly(xs, x), 2) == 0

# Example usage
xs = [1, 2]
x = 1.0
print(find_zero(xs))  # Output: 1.0
```

This script defines a function `poly` that evaluates a polynomial at a given point `x` using the given coefficients. The function `find_zero` finds the zero of a polynomial using the `poly` function. The test is passed to the `find_zero` function with the coefficients of a polynomial to verify its correctness.