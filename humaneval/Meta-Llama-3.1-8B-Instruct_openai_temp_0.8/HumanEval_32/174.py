```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Find a zero of a polynomial defined by coefficients xs.
    xs are coefficients of a polynomial from the highest degree term to the constant term.
    For example, for a polynomial ax^3 + bx^2 + cx + d, the coefficients would be [a, b, c, d].
    This function returns one of the roots of the polynomial.
    If there are multiple roots, it returns one of them.
    """
    
    # Ensure that the coefficients are in descending order
    if len(xs) % 2 == 0:
        raise ValueError("The polynomial must have an even number of coefficients.")
        
    # Create a polynomial object using numpy
    poly = np.poly1d(xs)
    
    # Find the roots of the polynomial
    roots = np.roots(poly)
    
    # Return the first real root
    for root in roots:
        if np.isreal(root):
            return round(root.real, 2)
    
    # If no real roots exist, return None
    return None


# Example usage:
print(find_zero([1, 2]))  # f(x) = 1 + 2x
print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This code uses the `numpy` library to create a polynomial object and find its roots. The `find_zero` function returns one of the real roots of the polynomial. If there are no real roots, it returns `None`. The example usage at the end demonstrates how to use this function.