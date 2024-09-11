### Polynomial Evaluation and Zero Finder

Below is a Python script that solves the given problem using the `numpy` library for efficient polynomial evaluation and the `numpy.roots` function for finding the roots of a polynomial.

```markdown
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    return np.polyval(xs[::-1], x)


def find_zero(xs: list):
    """
    Finds the zero of a polynomial with coefficients xs.
    xs are coefficients of a polynomial in ascending order of powers.
    find_zero returns the first zero point, even if there are many.
    """
    # Reverse the coefficients to get them in descending order of powers
    xs = xs[::-1]
    
    # Use numpy.roots to find the roots of the polynomial
    roots = np.roots(xs)
    
    # Return the first real root
    return roots[np.isreal(roots)][0].real
```

### Example Usage

```python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses the `numpy.polyval` function to efficiently evaluate polynomials at a given point, and the `numpy.roots` function to find the roots of a polynomial, which correspond to the zeros of the polynomial. The `find_zero` function returns the first real root of the polynomial.