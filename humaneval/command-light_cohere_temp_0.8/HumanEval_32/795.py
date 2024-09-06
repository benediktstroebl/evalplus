```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial x^n + xs[0] * x^(n-1) + xs[1] * x^(n-2) + ... = 0
    -0.5
    minimum power guarantee with x
    """
    return [x]


# Test cases
xs = [1, 2]
x = 2.5
print(poly(xs, x))  # 2.254832


xs = [-6, 11, -6, 1]
x = -1.0
print(poly(xs, x))  # -6.0 * x^3 + 11 * x^2 + x^3 -1.0
print(find_zero(xs))  # [-1.8]


xs = [1, 0, 1]
x = 0.0
print(poly(xs, x))  # 0.0 * x^2 + x
print(find_zero(xs))  # []


xs = [1, 0, -1]
x = -2.5
print(poly(xs, x))  # -1.0 * x^2 -0 + -1 * x^2 + (-1) * x^3
print(find_zero(xs))  # [-2.5, -2.4.0]