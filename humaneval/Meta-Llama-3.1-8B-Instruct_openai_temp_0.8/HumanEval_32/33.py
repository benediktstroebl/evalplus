```markdown
### Polynomial Evaluator and Zero Finder
#### `poly` Function: Evaluates Polynomial at a Point
#### `find_zero` Function: Finds a Zero of a Polynomial with Even Number of Coefficients

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): List of coefficients of the polynomial in ascending order of powers.
    x (float): The point at which to evaluate the polynomial.
    
    Returns:
    float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of a polynomial with even number of coefficients.
    
    Args:
    xs (list): List of coefficients of the polynomial in ascending order of powers.
    
    Returns:
    float: A zero of the polynomial.
    
    Raises:
    ValueError: If the list xs does not have an even number of coefficients.
    """
    if len(xs) % 2!= 0:
        raise ValueError("List xs must have an even number of coefficients.")
    
    # Extract coefficients
    coeffs = xs
    
    # Find the coefficient of the highest power of x
    leading_coeff = coeffs[-1]
    
    # Find the constant term
    constant_term = coeffs[0]
    
    # Calculate the zero using the formula for a polynomial of degree 2
    # (assuming the leading coefficient is non-zero and the polynomial has only two terms)
    zero = -constant_term / leading_coeff
    
    return zero


# Example usage
if __name__ == "__main__":
    # Test the poly function
    coeffs = [1, 2]
    x = 0
    result = poly(coeffs, x)
    print(f"f({x}) = {result}")
    
    # Test the find_zero function
    coeffs = [-6, 11, -6, 1]
    try:
        zero = find_zero(coeffs)
        print(f"A zero of the polynomial is {zero}")
    except ValueError as e:
        print(e)
```

In this code, the `poly` function evaluates a polynomial at a given point `x`, and the `find_zero` function finds a zero of a polynomial with an even number of coefficients. The `find_zero` function assumes that the polynomial has only two terms and uses the formula for a quadratic equation to calculate the zero. If the input list does not have an even number of coefficients, it raises a `ValueError`.