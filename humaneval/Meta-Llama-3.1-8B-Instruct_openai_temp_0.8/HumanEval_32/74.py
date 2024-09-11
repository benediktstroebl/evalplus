### Find Zero of a Polynomial

This script uses a numerical method, the Newton-Raphson method, to find a root of a polynomial.

```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): coefficients of the polynomial
    x (float): point at which to evaluate the polynomial
    
    Returns:
    float: the value of the polynomial at x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Find x such that poly(x) = 0.
    
    Args:
    xs (list): coefficients of the polynomial
    
    Returns:
    float: a root of the polynomial (there may be multiple)
    
    Raises:
    ValueError: if the number of coefficients is odd, or if the largest coefficient is zero
    """
    
    # Check that the number of coefficients is even
    if len(xs) % 2!= 0:
        raise ValueError("Number of coefficients must be even")
    
    # Check that the largest coefficient is non-zero
    if xs[-1] == 0:
        raise ValueError("Largest coefficient must be non-zero")
    
    # Initial guess
    x = 1.0
    
    # Tolerance and maximum number of iterations
    tol = 1e-6
    max_iter = 1000
    
    # Newton-Raphson method
    for _ in range(max_iter):
        # Evaluate the polynomial and its derivative at x
        f = poly(xs, x)
        f_prime = poly([i * coeff for i, coeff in enumerate(xs) if i > 0], x)
        
        # Check if the polynomial is zero
        if abs(f) < tol:
            return round(x, 6)
        
        # Update the guess
        x = x - f / f_prime
    
    # If we reach this point, we've run out of iterations
    raise RuntimeError("Failed to converge")

# Example usage:
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
print(round(find_zero([-3, 4, 5]), 2))  # 4-6x+5x^2
```

This script uses the Newton-Raphson method to find a root of a polynomial. It first checks that the number of coefficients is even and that the largest coefficient is non-zero. It then uses the Newton-Raphson method to update the guess until it finds a root or runs out of iterations. The Newton-Raphson method is a simple iterative method that is well-suited for finding roots of polynomials. However, it may not work for all polynomials (e.g. those with multiple roots), and it may run into convergence issues for polynomials with roots that are not close to the initial guess. 

To use this script, simply call the `find_zero` function with a list of coefficients. The function will return a root of the polynomial.