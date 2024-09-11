### Evaluating Polynomial and Finding Zero
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
        xs (list): List of coefficients of the polynomial.
        x (float): Point at which to evaluate the polynomial.

    Returns:
        float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero of a polynomial.

    Args:
        xs (list): List of coefficients of the polynomial, with the largest non-zero coefficient first.

    Returns:
        float: A zero of the polynomial.
    """
    if len(xs) % 2!= 0:
        raise ValueError("List of coefficients must have an even number of elements")
    if xs[0] == 0:
        raise ValueError("List of coefficients must have a non-zero constant term")

    # Use numpy's roots function to find all zeros
    coefficients = xs[::-1]  # Reverse the list of coefficients
    roots = np.roots(coefficients)

    # Return the first real zero
    real_roots = [root.real for root in roots if np.isreal(root)]
    if real_roots:
        return real_roots[0]
    else:
        raise ValueError("No real zero found")
```
This script uses NumPy to find the roots of the polynomial, which is more efficient and accurate than the original implementation. It first checks that the list of coefficients has an even number of elements and a non-zero constant term, and then reverses the list of coefficients to match the format required by NumPy's `roots` function. The script then returns the first real zero found, or raises an error if no real zero is found.

You can use this script to evaluate polynomials and find their zeros, like this:
```python
print(poly([1, 2], 0))  # Evaluates f(x) = 1 + 2x at x = 0
print(find_zero([1, 2]))  # Finds a zero of f(x) = 1 + 2x
print(find_zero([-6, 11, -6, 1]))  # Finds a zero of (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```