```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ 
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    
    Parameters:
    xs (list): List of coefficients of the polynomial.
    
    Returns:
    float: The zero point of the polynomial.
    
    Example:
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    
    # Ensure the input list is valid (even number of coefficients and largest non-zero coefficient)
    if len(xs) % 2!= 0 or xs[-1] == 0:
        raise ValueError("Input list must have an even number of coefficients and the largest non-zero coefficient")
    
    # Use Newton's method to find the root
    def derivative(xs, x):
        return sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs)])
    
    def newton_raphson(xs, x):
        return x - poly(xs, x) / derivative(xs, x)
    
    # Start with an initial guess
    x = -1
    
    # Run Newton's method until convergence
    for _ in range(100):
        x = newton_raphson(xs, x)
    
    return x

print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

In this corrected code, I have used Newton's method to find the root of the polynomial. Newton's method is a powerful technique for finding roots of a function and is particularly useful for polynomials. 

However, the use of `numpy` was removed from the code to maintain compliance with the original problem requirements.