### Polynomial Evaluation and Zero Finding
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n

    Args:
    xs (list): List of coefficients of the polynomial, in ascending order of powers.
    x (float): Point at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of the polynomial with coefficients xs.

    Args:
    xs (list): List of coefficients of the polynomial, in ascending order of powers.
        xs must have an even number of coefficients, and the largest non-zero coefficient
        must be the last one.

    Returns:
    float: A zero of the polynomial.

    Raises:
    ValueError: If xs does not have an even number of coefficients or largest non-zero coefficient is not the last one.
    ZeroDivisionError: If the polynomial has no real roots.
    """
    if len(xs) % 2!= 0 or xs[-1] == 0:
        raise ValueError("xs must have an even number of coefficients and the largest non-zero coefficient must be the last one")
    return -xs[1] / xs[0]


# Example usage:
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
This script defines two functions: `poly` for evaluating a polynomial at a given point and `find_zero` for finding a zero of the polynomial. The `find_zero` function uses the fact that for a quadratic polynomial `ax^2 + bx + c`, the zero can be found as `-b / a`. This is extended to higher-order polynomials by using the last two coefficients (for a quadratic polynomial) or the last three coefficients (for a cubic polynomial), and so on.