### Evaluating Polynomials and Finding Zeroes

Below is a Python script that uses the NumPy library to evaluate polynomials and find zeroes. The script uses the `numpy.roots` function to find the zeroes of a polynomial.

```markdown
### Code
```python
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return np.polyval(np.poly1d(xs), x)


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Ensure the coefficients list has an even number of elements
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")
    
    # Reverse and normalize the coefficients to match NumPy's expectations
    coeffs = np.array(xs[::-1]) / np.abs(np.max(xs[::-1]))
    
    # Find the roots of the polynomial
    roots = np.roots(coeffs)
    
    # Return the real part of the root with the largest magnitude
    return np.real(roots[np.argmax(np.abs(roots))])
```

### Example Usage

```python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note that the `numpy.roots` function returns complex roots, so we use `np.real` to extract the real part of the root with the largest magnitude.