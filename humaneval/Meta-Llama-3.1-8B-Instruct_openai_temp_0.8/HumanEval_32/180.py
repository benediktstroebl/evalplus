### Polynomial Solver
#### Problem: Find Zero of a Polynomial

This script provides a Python implementation of a polynomial solver. It uses the `numpy` library for efficient calculations and the `sympy` library for symbolic computations.

```python
import numpy as np
import sympy as sp

def poly(xs: list, x: sp.Symbol) -> sp.Expr:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * x**i for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    """
    Evaluates polynomial with coefficients xs at point x and finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    """
    x = sp.symbols('x')  # define symbolic variable x
    poly_expr = poly(xs, x)  # compute polynomial expression
    solution = sp.solve(poly_expr, x)  # solve for x
    if len(solution) > 0:
        return float(solution[0])  # return first solution as float
    else:
        return None  # return None if no solution found

# example usage
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note that we've used `sp.symbols('x')` to define a symbolic variable `x` and `sp.solve(poly_expr, x)` to find the zeros of the polynomial. The `solve` function returns a list of solutions, and we return the first one as a float.

This script assumes that you have both `numpy` and `sympy` installed. If not, you can install them via pip:

```bash
pip install numpy sympy
```