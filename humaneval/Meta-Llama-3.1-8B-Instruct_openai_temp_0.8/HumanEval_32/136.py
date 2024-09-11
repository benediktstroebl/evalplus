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
    Finds x such that poly(x) = 0.
    
    Args:
    xs (list): Coefficients of a polynomial.
    
    Returns:
    The x value where the polynomial equals zero.
    
    Note:
    This function only returns one zero point, even if there are many.
    It only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    
    # Check if xs has even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")
    
    # Find largest non-zero coefficient
    max_non_zero_coeff = max(coeff for coeff in xs if coeff!= 0)
    
    # Check if largest non-zero coefficient is the first one
    if xs.index(max_non_zero_coeff)!= 0:
        raise ValueError("largest non-zero coefficient must be the first one")
    
    # Initialize variables for Newton's method
    a = xs[1]
    b = -xs[0]
    c = 0
    
    # Newton's method to find the root
    while abs(a**2 - 3*b*c) > 1e-6:  # tolerance
        a_new = a
        b_new = (a**2 - b) / 3
        c_new = (2*a**3 - 9*a*b*c) / (27*a**2 - 2*b**2)
        
        a = a_new
        b = b_new
        c = c_new
    
    # return the root
    return -b / a

# Test cases
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script defines a polynomial evaluation function `poly` and a function `find_zero` for finding the root of a polynomial. The `find_zero` function uses Newton's method to find the root, and it assumes that the input polynomial has even number of coefficients and the largest non-zero coefficient as the first one in the list.