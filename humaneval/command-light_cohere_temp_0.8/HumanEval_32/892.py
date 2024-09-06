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
    find_zero finds x such that polynomial poly(x) = 0
    find_zero returns x and degree of polynomial at x
    """
    x0, degree = -inf, 0
    for x in range(1, 10):
        if poly(xs, x) == 0:
            x0, degree = x, 1
            break
    return x0, degree

# Test cases
test_cases = [
    [1, 2],
    [-6, 11, -6, 1],
    [-7, 4, -1, 7],
    [5, 8, 10, 5]
]

for test_case in test_cases:
    x0, degree = find_zero(test_case)
    assert x0 == test_case[0]
    assert degree == test_case[1]

```
The code above has a function called `find_zero` which finds the roots of polynomial equations. It takes a for a list of coefficients `xs` and returns the `x` value at which the polynomial equals zero. It takes `assert` statements to test if the function is working correctly.