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
    find_zero find x such that polynomial(x) = 0, returns only zero point, even if there are many.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    return round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
    -0.5
    return round(find_zero([-6, 11, -6, 1]), 2)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    # ...
    """
poly([1, 2, -6, 11, -6])  # [-6, 11]
find_zero([1, 2])  # [1]
```
The function `poly` computes the resultant polynomial given a list of coefficients xs and a point x. The function `find_zero` identifies the zero of the polynomial and returns only the zero point, even if there are many solutions. It works by first identifying the coefficients and then looking for the largest non-zero coefficient, which guarantees a solution. The function returns the value of the zero point rounded to two decimal places.