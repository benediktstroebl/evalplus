### Evaluating Polynomials and Finding Zeroes

Below is a Python script that evaluates polynomials and finds their zeroes.

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): coefficients of the polynomial
    x (float): point at which to evaluate the polynomial
    
    Returns:
    float: value of the polynomial at point x
    """
    # Using numpy's polyval function for more efficient polynomial evaluation
    return np.polyval(xs, x)

def find_zero(xs: list):
    """
    Finds a zero of the polynomial with coefficients xs.
    
    Args:
    xs (list): coefficients of the polynomial
    
    Returns:
    float: a zero of the polynomial
    """
    # Check if the polynomial has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("Polynomial must have an even number of coefficients")
    
    # Find the largest non-zero coefficient and its index
    max_coeff_idx = max((i for i, coeff in enumerate(xs) if abs(coeff) > 1e-9), default=None)
    
    if max_coeff_idx is None:
        raise ValueError("Polynomial must have at least one non-zero coefficient")
    
    # Evaluate the polynomial at the point where the largest coefficient is negative
    return -xs[max_coeff_idx - 1] / xs[max_coeff_idx]

# Example usage:
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

### Notes:

*   We use `numpy` to evaluate polynomials for more efficiency.
*   The `find_zero` function is modified to raise a `ValueError` if the polynomial does not have an even number of coefficients or if it has no non-zero coefficients.
*   We use a more efficient method to find the largest non-zero coefficient and its index.
*   The function returns a single zero of the polynomial, even if there are multiple zeroes.