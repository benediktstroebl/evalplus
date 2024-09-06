```python
import math
def evaluate_polynomial(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns a fact, x must be >= 0.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that the polynomial evaluated at x equals 0.
    Returns only one zero point, even if there are many.
    >
    takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    >>> evaluate_polynomial([1, 2], 2.0)  # 1 + 2 * 2.0
   
    unique zero value in the list.
    >>> evaluate_polynomial([-6, 11, -6, 1], 1.0)  # -6 -
    -0.5
```