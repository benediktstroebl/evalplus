```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial(x) = 0, returns only zero point, even if there are many.
    find_zero returns only zero point, even if there are many
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
```
xs = [1, 2]
xs = [-6, 11, -6, 1]
print(poly(xs, x)) # [0, 2] + x + 2 * x**2 + (-6) * x**(-1)
print(find_zero(xs)) # (-1)
```
The output will be the evaluation of the polynomial at x and the solution to the corresponding equation.