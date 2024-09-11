### Zero Finding in Polynomials
#### A Python Script to Find Zero Points of Polynomials
```python
import math
import sympy as sp  # Using sympy for polynomial operations

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n

    Args:
    xs (list): List of coefficients of the polynomial
    x (float): Point at which to evaluate the polynomial

    Returns:
    float: Value of the polynomial at point x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Find x such that poly(xs, x) = 0.
    Only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

    Args:
    xs (list): List of coefficients of the polynomial

    Returns:
    float: One zero point of the polynomial
    """
    # Convert list of coefficients to sympy polynomial
    x = sp.symbols('x')
    poly_expr = sum([coeff * x**i for i, coeff in enumerate(xs)])

    # Factor the polynomial
    factors = sp.factor(poly_expr)

    # Find the roots of the polynomial
    roots = sp.solve(factors, x)

    # Return the first root
    return float(roots[0])


# Test the function
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
Note that we're using the sympy library to handle polynomial operations. The `find_zero` function now uses sympy's `solve` function to find the roots of the polynomial. The `poly` function remains the same as in the original code.