### Finding a Zero of a Polynomial
#### Problem Description

This script evaluates a polynomial at a given point and finds a zero of a given polynomial.

#### Solution

```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): Coefficients of the polynomial in descending order.
    x (float): Point at which to evaluate the polynomial.
    
    Returns:
    float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero of the polynomial with coefficients xs.
    
    Args:
    xs (list): Coefficients of the polynomial in descending order.
              It is assumed that the list has an even number of coefficients
              and the largest non-zero coefficient is at an even index.
    
    Returns:
    float: A zero of the polynomial.
    """
    if len(xs) % 2!= 0 or xs[0] == 0:
        raise ValueError("Input list must have an even number of coefficients "
                         "and the largest non-zero coefficient at an even index.")
    
    a = xs[-2]
    b = xs[-1]
    
    # Find the zero using the quadratic formula
    x = -b / a
    return x

# Example usage:
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script evaluates a polynomial at a given point using the `poly` function and finds a zero of a given polynomial using the `find_zero` function. The `find_zero` function assumes that the input list has an even number of coefficients and the largest non-zero coefficient at an even index, and it uses the quadratic formula to find the zero. If these assumptions are not met, it raises a `ValueError`.