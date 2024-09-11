### Python Script to Find Zero of a Polynomial
```markdown
### Requirements
This script uses the `math` module for mathematical operations.

### Code
```python
import math


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
    Finds a zero of a polynomial with coefficients xs.

    Parameters:
    xs (list): coefficients of the polynomial. The list should have an even number of elements.
    
    Returns:
    float: a zero of the polynomial, or None if no solution is found

    Note: This function uses the quadratic formula to find a zero of the polynomial.
    It assumes that the largest non-zero coefficient is at an even index in the list xs,
    which guarantees that a solution exists.
    """
    # Extract coefficients
    n = len(xs)
    a = xs[n - 2]
    b = xs[n - 1]
    c = -xs[0]

    # Calculate the discriminant
    d = b**2 - 4*a*c

    # If the discriminant is negative, no real solution exists
    if d < 0:
        return None

    # Use the quadratic formula to find a zero
    x = (-b + math.sqrt(d)) / (2*a)

    return x
```

### Example Use Cases
```python
# Test the find_zero function
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

### Note
This script assumes that the list of coefficients xs has an even number of elements and that the largest non-zero coefficient is at an even index. This guarantees that a solution exists. If the discriminant is negative, the script returns None, indicating that no real solution exists.