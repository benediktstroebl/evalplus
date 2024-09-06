Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial == 0.
    Returns only the first found zero point for the polynomial, even if there are multiple zeros.

    Args:
        coefficients (list): Must contain an even number of coefficients for a polynomial ax^2 + bx + c,
                            with the largest non-zero coefficient.

    Returns:
        float: A solution x for the polynomial equation.
    """
    a, b, c = coefficients[:3]
    root1, root2 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return min(root1, root2)
```

This script includes two functions. The first function, `poly`, takes a list of coefficients and a value `x` as input, and returns the value of the polynomial with those coefficients evaluated at `x`. 

The second function, `find_zero`, takes a list of coefficients as input and returns the value of a zero point for the polynomial. This function only returns the first zero point found, even if there are multiple zero points. This function also only works with lists of coefficients that have an even number of coefficients and where the largest non-zero coefficient is present. 

These functions are designed to work with a polynomial of the form `ax^2 + bx + c`, and the input coefficients list contains the coefficients for this polynomial in the order `a`, `b`, `c`. 

Note that this script assumes that the input lists and numbers are valid and well-formed. Additional error handling and edge case handling can be included for more robust functionality.