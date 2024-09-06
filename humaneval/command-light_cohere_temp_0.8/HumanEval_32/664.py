```python
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    x0 = 0.0
    to be the absolute condition, meaning that the solution is unique and positive, 
    regardless of the number of coefficients in the polynomial.

xs = [1, 2]
print(find_zero(xs)) # f(x) = 1 + 2x - 0.5
xs = [6, 11, -6, 1]
print(find_zero(xs)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
The code is a good start, but you can still improve it by using the right way to write the functions, using the right variable names, and using better commenting and naming conventions.