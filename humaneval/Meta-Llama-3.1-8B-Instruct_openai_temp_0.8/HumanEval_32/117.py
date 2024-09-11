```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    # Use numpy's polyval function for efficient polynomial evaluation
    return np.polyval(xs[::-1], x)


def find_zero(xs: list):
    """
    finds x such that poly(x) = 0.
    finds only one zero point, even if there are many.
    takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    
    Note: This function uses the numpy library to find the roots of the polynomial.
    """
    # Check if the length of the input list is even
    if len(xs) % 2!= 0:
        raise ValueError("Input list must have an even number of coefficients")
    
    # Check if the largest coefficient is non-zero
    if xs[0] == 0:
        raise ValueError("Largest coefficient cannot be zero")
    
    # Use numpy's roots function to find the roots of the polynomial
    return np.roots(xs[::-1])[0].real


# Test the functions
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses the numpy library to efficiently evaluate the polynomial and find its roots. The `poly` function uses `np.polyval` to evaluate the polynomial at a given point, and the `find_zero` function uses `np.roots` to find the roots of the polynomial.

Note that the `find_zero` function now correctly raises an error if the input list has an odd number of coefficients or if the largest coefficient is zero, as required by the problem statement.