Here's how you could implement the function `find_zero` using a numerical method to find roots of a polynomial. I'll use the `numpy` library for its efficient and stable polynomial solver.

```markdown
### Numerical Polynomial Solver
#### Using numpy's roots function

```python
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * x**i for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Find a root of a polynomial.
    
    Args:
    xs (list): coefficients of a polynomial in descending order of powers.
    
    Returns:
    A root of the polynomial.
    """
    # Ensure the coefficients are in descending order of powers
    xs = xs[::-1]
    
    # Use numpy's roots function to find all roots
    roots = np.roots(xs)
    
    # Return the first root
    return roots[0].real

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note: The `numpy.roots` function returns complex roots. In this case, we return only the real part of the root.

Also note: This function returns only one root, even if the polynomial has multiple roots. The number of roots is determined by the degree of the polynomial. For example, a polynomial of degree 1 has exactly one root, a polynomial of degree 2 has at most two roots, and so on.