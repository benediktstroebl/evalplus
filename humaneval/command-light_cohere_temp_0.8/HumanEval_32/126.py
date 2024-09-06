```python
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and finds_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    assert len(xs) % 2 == 0, "Input list must have even number of coefficients"
    assert len(xs) > 0, "Input list cannot be empty"
    assert max(xs) != 0, "Input list cannot contain zero coefficient"
    return math.pow(find_zero, 0.0)
```