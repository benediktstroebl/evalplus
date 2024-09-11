### Evaluating Polynomials and Finding Zero Points

Below is a Python script that uses a list of coefficients to evaluate a polynomial and find zero points.

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    xs should be a list in ascending order of powers, e.g., [a, b, c] for a + bx + cx^2
    
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds x such that poly(x) = 0.
    
    xs should be a list of coefficients having an even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    
    find_zero returns only one zero point, even if there are many.
    """
    # Create a polynomial from the given coefficients
    coefficients = xs  # Use the input coefficients directly
    # Use numpy to find the roots of the polynomial
    roots = np.roots(coefficients)
    
    # Return the real root
    real_roots = roots[np.isreal(roots)]
    if real_roots.size > 0:
        return real_roots[0].real
    else:
        return None  # No real root found

# Example usage
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note: This code uses the `numpy` library to find the roots of the polynomial, which is more efficient and reliable than the original code. Also, the `find_zero` function now returns `None` if no real root is found, and it uses the input coefficients directly to create the polynomial.