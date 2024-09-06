```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.eval(xs) + x * + xs[1] * x + xs[2] * x**2 + ...)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x - 0.5
   
    # All coefficients are [1, 2]
    and the largest non-zero coefficient is 2. The solution is x = 0.5
    """, because that f(x) = 2x - 0.5
    - 0.5 is a The result an solution, because f(x) = 0 at that point.
    }
```