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
    find_zero find x such that the polynomial is zero, i.
    find_zero returns only zero point, even if there are many solutions
    and find_zero only takes list xs having even number of coefficients and largest non zero coefficient guarantees a solution.
    return x
    for x in [x for x in xs if x != 0 and math.pow(x, x) == 0]
    return x


# test cases
xs = [1, 2]
x = 1.0
print(poly(xs, x))  # prints 2
x = 2.0
print(poly(xs, x))  # prints 4
x = 3.0
print(poly(xs, x))  # prints 8
print(find_zero(xs))  # prints 2
```