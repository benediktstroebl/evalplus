Here's how you can implement the functions using the NumPy library for numerical operations and the `numpy.roots` function for finding the roots of a polynomial. This approach is more efficient and handles polynomials of any degree.

```python
import numpy as np


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * x**i for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only the first zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Ensure xs has an even number of coefficients
    assert len(xs) % 2 == 0, "Coefficients must have an even number"

    # The largest non-zero coefficient must be the first one
    assert xs[0]!= 0, "Largest non-zero coefficient must be the first one"

    # Reverse the coefficients to match the numpy.roots function's format
    coeffs = xs[::-1]

    # Use numpy.roots to find the roots of the polynomial
    roots = np.roots(coeffs)

    # Return the first root (which is the first zero point)
    return roots[0]
```

You can test the `find_zero` function with the examples provided:

```python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```