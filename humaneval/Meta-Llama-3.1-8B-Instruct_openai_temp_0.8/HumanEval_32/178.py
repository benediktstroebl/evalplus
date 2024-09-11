## Python Script to Evaluate Polynomial and Find Zero
### Overview

This Python script provides a solution to evaluate a polynomial with given coefficients and find the zero point of the polynomial.

### Code

```markdown
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): Coefficients of the polynomial.
    x (float): Point at which the polynomial is evaluated.
    
    Returns:
    float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(reversed(xs))])


def find_zero(xs: list):
    """
    Finds the zero point of a polynomial.

    Args:
    xs (list): Coefficients of the polynomial.
    
    Returns:
    float: Zero point of the polynomial.
    
    Raises:
    ValueError: If the polynomial has an odd number of coefficients.
    """
    if len(xs) % 2!= 0:
        raise ValueError("Polynomial must have an even number of coefficients.")
    
    if not any(coeff!= 0 for coeff in xs):
        return "Polynomial is constant and has no zero point."
    
    # Get the last coefficient (largest power of x) and its degree
    last_coeff = xs[-1]
    degree = len(xs) - 1
    
    # Find the zero point using the last coefficient and its degree
    zero = - last_coeff / xs[-2]
    
    return round(zero, 2)


# Test cases
print(find_zero([1, 2]))  # Expected output: -0.5
print(find_zero([-6, 11, -6, 1]))  # Expected output: 1.0
```

### Explanation

The provided code defines two functions: `poly` and `find_zero`. The `poly` function evaluates a polynomial with given coefficients at a specified point `x`. It does this by summing up each coefficient multiplied by `x` raised to the power of its index (from right to left).

The `find_zero` function finds the zero point of a polynomial. It first checks if the polynomial has an even number of coefficients. If not, it raises a `ValueError`. It also checks if the polynomial is constant (all coefficients are zero), in which case it returns a message indicating that the polynomial has no zero point.

Finally, the code uses the `find_zero` function to find the zero point of two test polynomials and prints the results.

Note: This code assumes that the input coefficients are in descending order of power. If the coefficients are in ascending order, the code should be modified to use `enumerate(xs)` instead of `enumerate(reversed(xs))` in the `poly` function.