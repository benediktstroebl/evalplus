Here is the Python script that solves the problem:
```markdown
### Polynomial Evaluation and Root Finding Script

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def poly_np(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x using numpy.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return np.polyval(np.array(xs), x)

def find_zero(xs: list):
    """
    Finds a zero of the polynomial defined by the coefficients xs.
    xs must have an even number of coefficients and the largest non-zero coefficient must be the first.
    Returns only one zero point.
    """
    # Check if the list has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("The list of coefficients must have an even number of elements")

    # Check if the largest non-zero coefficient is the first
    if xs[0] == 0:
        raise ValueError("The largest non-zero coefficient must be the first")

    # Use numpy to find the roots of the polynomial
    roots = np.roots(np.array(xs))
    
    # Return the first real root
    real_roots = [root.real for root in roots if root.imag == 0]
    return real_roots[0] if real_roots else None

# Example usage
if __name__ == "__main__":
    print("Evaluating polynomial 1 + 2x at x = 0:")
    print(poly([1, 2], 0))
    print(poly_np([1, 2], 0))
    
    print("\nFinding zero of polynomial -6 + 11x - 6x^2 + x^3:")
    print(find_zero([-6, 11, -6, 1]))
```

This script uses numpy's `polyval` and `roots` functions to efficiently evaluate the polynomial and find its roots. The `find_zero` function checks if the input list has an even number of coefficients and the largest non-zero coefficient is the first, and then uses `numpy.roots` to find the roots of the polynomial. It returns the first real root.

Note that the `find_zero` function may not always find the correct root, especially for polynomials with multiple roots. For such cases, you may need to use a more advanced root-finding algorithm.