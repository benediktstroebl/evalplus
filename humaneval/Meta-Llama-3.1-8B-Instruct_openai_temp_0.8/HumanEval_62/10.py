### Calculating the Derivative of a Polynomial

Below is a Python function using numpy that calculates the derivative of a polynomial given its coefficients.

```python
import numpy as np

def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial.
               The first element (xs[0]) is the constant term.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    """
    # Remove the constant term (xs[0]) and multiply each remaining coefficient by its index
    derivative_coeffs = [i * x for i, x in enumerate(xs[1:], start=1)]
    
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. It uses a list comprehension to generate the coefficients of the derivative polynomial, where each coefficient is the product of its index and the corresponding coefficient in the original polynomial. The function then returns this list of coefficients.

The script also includes two test cases to verify that the function works correctly.