```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes polynomial(x) = 0, returns only zero point, even if there are many.
    """
    -1. Convert xs to set
    - to a numpy array with n coefficients.
    -2. Calculate determinant of polynomial using
    - use de l'Hospital's formula
    -3. Find x_zero, the value of x that makes the determinant negative
    -4. Return x_zero


# Example
xs = [1, 2]
x = find_zero(xs)
print(f'x = {x}')
```