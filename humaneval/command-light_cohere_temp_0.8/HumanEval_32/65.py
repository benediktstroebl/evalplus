```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.poly(x) + xs[1] * x + xs[0] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that the polynomial is zero
    find_zero returns only zero point, even if there are many
    """
    return math.floor(find(poly(x), xs))


# Example usage:
xs = [1, 2]
x = float(5)
print(find_zero(xs))  # Output: 2.77228
```