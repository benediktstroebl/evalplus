### Newton-Raphson Method for Finding Polynomial Roots

Below is a Python script that uses the Newton-Raphson method to find roots of a polynomial.

```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def derivative(xs: list, x: float):
    """
    Evaluates derivative of polynomial with coefficients xs at point x.
    return xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 +.... n * xs[n] * x^(n-1)
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs)])

def find_zero(xs: list, max_iter: int = 1000, tol: float = 1e-5):
    """
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    
    Parameters:
    xs (list): coefficients of a polynomial.
    max_iter (int): maximum number of iterations for Newton-Raphson method.
    tol (float): tolerance for convergence of Newton-Raphson method.
    
    Returns:
    float: root of the polynomial.
    """
    # Initialize guess for the root
    x = 1.0
    
    for _ in range(max_iter):
        # Newton-Raphson method update
        x_next = x - poly(xs, x) / derivative(xs, x)
        
        # Check for convergence
        if abs(x_next - x) < tol:
            return round(x_next, 2)
        
        x = x_next
    
    # If max_iter is reached, return the last estimate
    return round(x, 2)

# Test the function
print(find_zero([1, 2]))  # f(x) = 1 + 2x
print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses the Newton-Raphson method to find the roots of a polynomial. The `find_zero` function takes a list of coefficients `xs`, and returns the root of the polynomial. The function first initiates a guess for the root as `1.0`. It then iteratively updates the guess using the Newton-Raphson method formula until convergence is reached or `max_iter` is exceeded. The function returns the root rounded to two decimal places.