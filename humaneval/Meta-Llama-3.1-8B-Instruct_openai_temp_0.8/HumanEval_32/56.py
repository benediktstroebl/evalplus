### Finding the Zero of a Polynomial
#### Description
This script defines a function `poly` to evaluate a polynomial at a given point `x`, and the function `find_zero` to find the zero of the polynomial.

#### Code
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): coefficients of the polynomial
    x (float): point at which to evaluate the polynomial
    
    Returns:
    float: the value of the polynomial at point x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds the zero of a polynomial with given coefficients.
    
    Args:
    xs (list): coefficients of the polynomial
    
    Returns:
    float: the zero of the polynomial
    
    Raises:
    ValueError: if xs has an odd number of coefficients
    """
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")
    
    # Find the largest non-zero coefficient
    non_zero_coeffs = [coeff for coeff in xs if coeff!= 0]
    largest_non_zero = max(non_zero_coeffs)
    
    # Find the zero of the polynomial
    zero_index = xs.index(largest_non_zero)
    return -math.pow(largest_non_zero, -1) * math.pow(-1, (zero_index - 1) // 2) * math.pow(largest_non_zero, 1 - (zero_index - 1) // 2) / (zero_index - 1) // 2


# Example usage:
print("f(x) = 1 + 2x:", round(find_zero([1, 2]), 2))
print("(x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3:", round(find_zero([-6, 11, -6, 1]), 2))
```

#### Explanation
The `find_zero` function first checks if the list of coefficients `xs` has an even number of elements. If not, it raises a `ValueError`. Then, it finds the largest non-zero coefficient and uses it to find the zero of the polynomial. The formula used is based on the fact that the zero of the polynomial can be found by taking the reciprocal of the largest non-zero coefficient and dividing it by the index of the coefficient minus one, divided by two. This formula is derived from the properties of polynomial roots and the relationship between the coefficients and the roots.