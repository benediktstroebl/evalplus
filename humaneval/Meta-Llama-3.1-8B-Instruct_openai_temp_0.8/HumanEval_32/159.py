### Polynomial Evaluation and Zero Finding
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * x**i for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial with coefficients xs.
    xs are coefficients of a polynomial in descending order of powers.
    find_zero returns only one zero point, even if there are many.
    xs can have any number of coefficients, not just an even number.
    """
    # Use numpy to find the roots of the polynomial
    roots = np.roots(xs)
    
    # The find_zero function will return the first real root
    real_roots = [root.real for root in roots if np.isreal(root)]
    return real_roots[0] if real_roots else None

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
### Explanation:

The provided code uses NumPy's `np.roots` function to find the roots of the polynomial. This function returns all roots of the polynomial, including complex ones. We then filter the roots to keep only the real ones and return the first one.

Note that the `find_zero` function can handle polynomials with any number of coefficients, not just an even number. The `np.roots` function can handle polynomials of any degree.