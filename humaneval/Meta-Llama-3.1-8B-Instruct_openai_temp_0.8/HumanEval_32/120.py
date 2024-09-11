### Polynomial Evaluation and Zero Finder
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Parameters:
    xs (list): coefficients of the polynomial
    x (float): point at which to evaluate the polynomial
    
    Returns:
    float: value of the polynomial at point x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial given its coefficients.
    
    Parameters:
    xs (list): coefficients of the polynomial
    
    Returns:
    float: a zero point of the polynomial
    """
    # Check if the list has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("List must have an even number of coefficients")
    
    # Find the largest non-zero coefficient
    non_zero_coeffs = [coeff for coeff in xs if coeff!= 0]
    if not non_zero_coeffs:
        raise ValueError("List must have at least one non-zero coefficient")
    largest_coeff = max(non_zero_coeffs)
    
    # Check if the polynomial has degree 0
    if len(non_zero_coeffs) == 1:
        return -largest_coeff
    
    # Find the x value such that poly(x) = sum(xs)
    x = sum(xs) / largest_coeff
    
    return x

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
Alternatively, you could use the `numpy` library to implement a more robust and efficient polynomial evaluation and zero finding algorithm:
```python
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Parameters:
    xs (list): coefficients of the polynomial
    x (float): point at which to evaluate the polynomial
    
    Returns:
    float: value of the polynomial at point x
    """
    return np.polyval(xs, x)

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial given its coefficients.
    
    Parameters:
    xs (list): coefficients of the polynomial
    
    Returns:
    float: a zero point of the polynomial
    """
    # Check if the list has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("List must have an even number of coefficients")
    
    # Find the largest non-zero coefficient
    non_zero_coeffs = [coeff for coeff in xs if coeff!= 0]
    if not non_zero_coeffs:
        raise ValueError("List must have at least one non-zero coefficient")
    largest_coeff = max(non_zero_coeffs)
    
    # Check if the polynomial has degree 0
    if len(non_zero_coeffs) == 1:
        return -largest_coeff
    
    # Find the x value such that poly(x) = sum(xs)
    x = sum(xs) / largest_coeff
    
    return x

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) *