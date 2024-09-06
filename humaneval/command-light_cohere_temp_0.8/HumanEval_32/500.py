```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns x, even if there are many roots.
    """
    take list xs having even number of coefficients and largest non-zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -1.0
    """ next = - smallest positive value in xs[0] to xs[1] to xs[2]
    """
    return next(xs)

# Test cases
test_cases = [
    (1, 2),
    (-6, 11, -6, 1),
    (1, -3, -2, -4),
]

test_run = [
    poly,
    find_zero,
    0,
]

for case, f in enumerate(test_run):
    try:
        result = f(case)
        print(f" Test {case}: {result}")
except ZeroDivisionError:
        print(f" Test {case}: polynomial division by zero")
except Exception as e:
        print(f" Test {case}: {e}")
``` 
The output will show the results for each test case.