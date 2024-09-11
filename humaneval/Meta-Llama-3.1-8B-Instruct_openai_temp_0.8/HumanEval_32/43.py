### Polynomial Evaluation and Root Finding
#### Problem Description
Find the root of a polynomial given its coefficients. The polynomial should have an even number of coefficients and the largest non-zero coefficient should be at an even index.

#### Solution
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds x such that poly(x) = 0 for a given polynomial with coefficients xs.
    
    Args:
    xs (list): coefficients of the polynomial. The largest non-zero coefficient should be at an even index.
    
    Returns:
    float: the root of the polynomial.
    """
    # Check if the largest non-zero coefficient is at an even index
    max_coeff = max([coeff for coeff in xs if coeff!= 0])
    max_index = xs.index(max_coeff)
    if max_index % 2!= 0:
        raise ValueError("The largest non-zero coefficient should be at an even index")

    # Find the root using Newton's method with an initial guess of 0
    x = 0
    while abs(poly(xs, x)) > 1e-6:
        x_next = x - poly(xs, x) / sum([i * coeff for i, coeff in enumerate(xs) if i!= 0])
        x = x_next

    return x

# Test the functions
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
This script first checks if the largest non-zero coefficient is at an even index, as required by the problem. If not, it raises a ValueError. It then uses Newton's method to find the root of the polynomial. The initial guess for Newton's method is 0, and the method stops when the absolute value of the polynomial evaluated at the current guess is less than 1e-6. The script finally tests the functions with two examples.