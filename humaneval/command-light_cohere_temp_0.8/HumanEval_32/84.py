```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    """
    solve polynomial equations by "guessing" solutions until failure or success.

    guess, for x in [0, 1/x, sqrt(x), x+1, ...];

    # failure when x < 0, i.ve when x > 1, square roots of x in this range.
    # success when x > 0 and x <= 1
    return [x for x in (success if x >= 0) + [x for x in (failure if x > 1)] if success else None
    return [x]


# Test
xs = [1, 2]
x = find_zero(xs)
print(x)
```
This Python script defines a function find_zero that finds and returns the zero of a polynomial represented as a list of coefficients xs. The test case demonstrates this run the polynomial evaluation at the found point and prints the result.