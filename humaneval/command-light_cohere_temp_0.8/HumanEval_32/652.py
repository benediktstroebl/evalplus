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
    find_zero find x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    """
    note that we might find multiple solutions, and we only take the largest one, as it guarantees
    a solution.
# Test cases
    test_cases = [
        (1, 2),
        (-6, 11),
        (1.5, -9)
    ]
    assert find_zero(test_cases) == [(1.5, -9)
    ```