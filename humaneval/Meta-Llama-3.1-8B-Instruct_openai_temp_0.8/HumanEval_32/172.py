```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    n = len(xs)
    if n % 2!= 0:  # Check if the number of coefficients is even
        raise ValueError("List xs must have an even number of coefficients")

    # Find the largest non-zero coefficient
    largest_coeff = max(coeff for coeff in xs if coeff!= 0)

    # Initialize the interval [a, b] to search for the root
    a, b = -1, 1  # This is a reasonable starting interval

    # Perform binary search to find the root
    while a <= b:
        c = (a + b) / 2
        f_c = sum([coeff * math.pow(c, i) for i, coeff in enumerate(xs)])
        f_a = sum([coeff * math.pow(a, i) for i, coeff in enumerate(xs)])
        f_b = sum([coeff * math.pow(b, i) for i, coeff in enumerate(xs)])

        # Check if we have found the root
        if abs(f_c) < 1e-6:  # Tolerance for floating point comparison
            return round(c, 2)

        # Update the interval
        elif f_c * f_a > 0:
            a = c
        else:
            b = c

    # If we failed to find the root within the interval [-1, 1]
    # try to find it using numpy
    try:
        roots = np.roots(xs)
        return round(roots[0].real, 2)  # Return the real part of the root
    except np.linalg.LinAlgError:
        raise ValueError("Polynomial does not have a real root")

# Test the find_zero function
assert round(find_zero([1, 2]), 2) == -0.5  # f(x) = 1 + 2x
assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```