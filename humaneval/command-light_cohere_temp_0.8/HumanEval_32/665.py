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
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions
    """
    if len(xs) == 0:
        return None  # empty list means no solution

    largest_nonzero_coeff = max(xs)
    solution = xs[0] / largest_nonzero_coeff
    return solution


test_values = [1, 2, -6, 11, -6, 1]
test_result = find_zero(test_values)

if test_result is not None:
    print("The solutions are:", test_result)
else:
    print("No solutions.")
```
The function `find_zero` in this script identifies the x value that makes the provided polynomial equation equal to zero. This is then try each test values until it finds a solution or runs out of tests.