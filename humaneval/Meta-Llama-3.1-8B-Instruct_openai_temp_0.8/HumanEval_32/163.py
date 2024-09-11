### Solution: Find Zero of a Polynomial
```python
import math
import numpy as np


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
        xs (list): List of coefficients.
        x (float): Point at which the polynomial is evaluated.

    Returns:
        float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """
    Finds a zero point of a polynomial.

    Args:
        xs (list): List of coefficients. Must have an even number of elements and
            the largest non-zero coefficient must be the last one.

    Returns:
        float: A zero point of the polynomial.
    """
    n = len(xs)
    if n % 2!= 0:
        raise ValueError("List must have an even number of elements")

    # Use numpy to find roots of the polynomial
    # numpy.roots returns roots of the polynomial a_n*x^n + a_(n-1)*x^(n-1) +... + a_1*x + a_0
    # So we need to reverse the list of coefficients and change the sign of the first one
    # This will give us the coefficients in the form a_0 + a_1*x + a_2*x^2 +... + a_n*x^n
    coeffs = list(reversed(xs[:-1])) + [-xs[-1]]

    # Find roots of the polynomial
    roots = np.roots(coeffs)

    # The problem statement says that we are looking for a zero point, even if there are many
    # So we just take the first root
    return float(roots[0])
```

### Example Usage
```python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
Note: The numpy library is used to find the roots of the polynomial. The `numpy.roots` function returns an array of complex roots, so we need to convert the first root to a float.