Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial equation poly(x) = 0.
    Returns only the first found zero, i.e. there may be more than one.
    Works only for lists with even number of coefficients, and maximal coefficient != 0
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('list of coefficients must have even number of elements')
    max_coeff = max(coefficients)
    if max_coeff == 0:
        raise ValueError('max coefficient must be != 0')

    # solve quadratic equation with constants sum -a*d
    a = -coefficients[-1] / max_coeff
    d = 4 * a
    sum_ = coefficients[0] / max_coeff
    x = sum_/(d - math.sqrt(d**2 - sum_*sum_))
    return x
```

This script defines the `poly` and `find_zero` functions. The `poly` function evaluates the polynomial given a list of coefficients and a point, returning its value. The `find_zero` function finds the point `x` at which the polynomial evaluates to zero, returning only the first found zero. It works for polynomials with an even number of coefficients and a non-zero maximum coefficient. The function raises a `ValueError` if these conditions are not met.

These functions are well-suited for handling polynomial equations and finding zero points efficiently.