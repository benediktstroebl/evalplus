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
    and finds_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
# Example:  takes a test polynomial, checks if find_zero returns the correct solution
    assert find_zero([1, 2]) == 0.0
    # Test case 2:
    assert find_zero([-6, 11, -6, 1]) == -1.2

You can use this script to evaluate your polynomial functions and pass the tests.