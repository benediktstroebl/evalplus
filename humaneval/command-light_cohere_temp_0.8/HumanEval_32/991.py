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
    find_zero find x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    # Ensure list has even coefficients with even number.
    # largest non zero coefficient as it guarantees a solution.
    return round(poly(x), 2)
    """
    return x


# Example usage
xs = [1, 2]
x = find_zero(xs)
print(x)
```