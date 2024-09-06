```python
import math
def evaluate_poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x,
    returns sum(coefficient * math.pow(x) for coefficient in xs)
    """
    return sum([coef * math.pow(x) for coef in xs])
def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial
    find_zero finds x such that the polynomial is zero,
    returns only zero point, even if there are many,
    and find_zero only takes list xs having even number of coefficients
    and largest non-zero coefficient,
    because it guarantees a solution.
    x = xs[0]
    y = xs[1]
    while True:
        x += 1
        if x == float('inf') or x == float('-inf'):
            break
        if evaluate_poly(xs, x) == 0:
            return x
```