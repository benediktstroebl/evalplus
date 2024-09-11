### Finding Roots of Polynomial

Below is the Python script that implements the `poly` and `find_zero` functions. It uses a numerical method called Newton-Raphson to find the root of the polynomial.

```markdown
### polynomial_roots.py

```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
        xs (list): coefficients of the polynomial, e.g., [1, 2] for f(x) = 1 + 2x
        x (float): point at which to evaluate the polynomial
        
    Returns:
        float: value of the polynomial at point x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds the root of a polynomial with coefficients xs.
    
    Args:
        xs (list): coefficients of the polynomial, e.g., [1, 2] for f(x) = 1 + 2x
        
    Returns:
        float: root of the polynomial
    
    Raises:
        ValueError: if the input list xs does not have an even number of coefficients
    """
    if len(xs) % 2!= 0:
        raise ValueError("Input list must have an even number of coefficients")

    # Start with an initial guess for the root
    x = 1.0
    
    # Newton-Raphson method
    for _ in range(100):
        # Compute the derivative of the polynomial at point x
        dx = len(xs)
        derivative_x = sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs)])
        
        # Update the guess for the root
        x = x - poly(xs, x) / derivative_x
        
        # Check for convergence
        if abs(poly(xs, x)) < 1e-6:
            break
    
    return x

if __name__ == "__main__":
    # Test the functions
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script first checks if the input list `xs` has an even number of coefficients. If not, it raises a `ValueError`. Otherwise, it uses the Newton-Raphson method to find the root of the polynomial. It starts with an initial guess for the root, computes the derivative of the polynomial at the current guess, and updates the guess until the polynomial value at the guess is close to zero (within a tolerance of 1e-6). The script then prints the found root for the given test cases.