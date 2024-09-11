### Find Zero of a Polynomial
#### Python Script

```markdown
### Import necessary libraries
import math
import numpy as np

### Define a function to evaluate a polynomial
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
        xs (list): A list of coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.
    
    Returns:
        float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

### Define a function to find zero of a polynomial
def find_zero(xs: list):
    """
    Finds the zero of a polynomial with coefficients xs.
    
    Args:
        xs (list): A list of coefficients of the polynomial.
    
    Returns:
        float: The zero of the polynomial.
    
    Raises:
        ValueError: If the list xs does not have an even number of coefficients.
    """
    if len(xs) % 2!= 0:
        raise ValueError("The list xs must have an even number of coefficients.")
    
    # Get the coefficients of the polynomial
    coeffs = xs[::-1]
    
    # Use numpy to find the roots of the polynomial
    roots = np.roots(coeffs)
    
    # Return the real root
    return np.real(roots[np.isreal(roots)])[0]

### Test the function
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script first defines a function `poly` to evaluate a polynomial at a given point. It then defines a function `find_zero` to find the zero of a polynomial. This function uses `numpy` to find the roots of the polynomial, and returns the real root. The script also includes some test cases to demonstrate the usage of the `find_zero` function.