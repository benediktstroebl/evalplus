### Solution

Here's the Python script to solve the problem:

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
    Finds x such that poly(x) = 0 for a polynomial with coefficients xs.
    The function only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    Returns the zero point.
    
    Parameters:
    xs (list): coefficients of a polynomial
    
    Returns:
    float: x such that poly(x) = 0
    """
    # Ensure xs has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")
    
    # Check if the largest coefficient is zero
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient is required")
    
    # Use numpy's roots function to find the roots of the polynomial
    coeffs = xs[::-1]  # Reverse the coefficients to match numpy's convention
    roots = np.roots(coeffs)
    
    # Return the first real root
    for root in roots:
        if np.isreal(root):
            return root.real
    
    # If no real roots are found, return None
    return None

# Example usage:
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses NumPy's `roots` function to find the roots of the polynomial, which is more efficient and accurate than using a manual method. The `find_zero` function checks if the input list `xs` has an even number of coefficients and raises an error if not. It also checks if the largest coefficient is zero and raises an error if so. Finally, it returns the first real root of the polynomial.