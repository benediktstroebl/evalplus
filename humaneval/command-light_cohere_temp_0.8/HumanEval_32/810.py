```python
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    Furthermore, find_zero only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
    template is implemented in solve_problem(list, float) where list is the coefficients of a polynomial and float is the point to evaluate it at:
        solve_problem(xs, x):
            return None if any(xs) == 0 else poly(xs, x)

```
Here, the function solve_problem() serves as a wrapper for the above two functions and allows to pass different coefficients and points to evaluate the polynomial at.