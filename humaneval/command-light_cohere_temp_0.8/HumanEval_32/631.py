```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial equal to 0, returns only zero point, even if there are many.
    find_zero returns only zero point, even if there are many.
    """
    largest non zero coefficient and coefficients, since it guarantees a solution
    """
    if len(xs) < 2:
        return None  # insufficient data, cannot find a root
    elif len(xs) == 2:
        return [0]  # only one root, p = 1
    elif len(xs) > 2:
        return [x for x in range(1, len(xs)) if xs[x] != 0]  # cycle through coefficients, find non zero coefficients


xs = [1, 2]  # example input
x = 0.0
result = poly(xs, x)
print("poly evaluation:", result)
print("zero evaluation:", find_zero(xs))
```
This script defines a function `poly` that evaluates a polynomial at a given point `x`. It also defines a function `find_zero` that finds and returns the zero point of the polynomial, which is a root of the polynomial.

The script then demonstrates the functions by evaluating the polynomial at `x = 0` and finding the zero point of the polynomial using the `find_zero` function.