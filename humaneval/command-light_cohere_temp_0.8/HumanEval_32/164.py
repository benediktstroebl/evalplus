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
    find_zero finds x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many.
    The, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    assert len(xs) % 2 == 0, "Input must be a list of even number of coefficients."
    assert len(xs) > 0, "Input must not be empty"
    assert len(xs) == len(xs[0]) + 1, "All coefficients must have a corresponding term"
    assert xs[0] <= 0 and xs[0] != float("inf"), "First coefficient must be non negative"
    return xs[0]
```