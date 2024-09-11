```python
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n

    Args:
        xs (list): coefficients of the polynomial
        x (float): point at which to evaluate the polynomial

    Returns:
        float: value of the polynomial at point x
    """
    return sum([coeff * np.power(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Find a zero point of a polynomial with coefficients xs.

    Args:
        xs (list): coefficients of the polynomial, in descending order of powers

    Returns:
        float: one zero point of the polynomial
    """
    if len(xs) % 2!= 0:
        raise ValueError("Polynomial must have an even number of coefficients")

    # Find the largest non-zero coefficient
    i = max((i for i, coeff in enumerate(xs) if coeff!= 0), default=None)

    # If all coefficients are zero, there is no solution
    if i is None:
        raise ZeroDivisionError("Cannot find zero point of a zero polynomial")

    # Use numerical method to find a zero point
    return np.roots([xs[i] * (-1)**(len(xs)-i-1)] + [0] * i + [1])[0].real


# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note: This code uses the `numpy` library to efficiently evaluate polynomials and find roots. It assumes that the input coefficients are in descending order of powers. If the input coefficients are not in the correct order, the polynomial will be evaluated incorrectly. 

Also, this code does not guarantee to find the exact roots of the polynomial, especially for polynomials of degree higher than 2. It uses a numerical method (`np.roots`) to find an approximate root. For polynomials of degree 2 or less, it is possible to find an exact root using algebraic methods. If you need to find exact roots, you may need to use a different approach.