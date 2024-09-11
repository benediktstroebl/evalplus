### Polynomial Evaluation and Zero Finding

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
    xs (list): coefficients of the polynomial
    
    Returns:
    float: a zero point of the polynomial
    """
    # Ensure the list has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")

    # Find the largest non-zero coefficient
    max_coeff = max(coeff for coeff in xs if coeff!= 0)
    
    # Initialize the interval for the zero point
    a = -1
    b = 1
    
    # Perform binary search to find the zero point
    while abs(b - a) > 1e-5:
        c = (a + b) / 2
        val = poly(xs, c)
        if val == 0:
            break
        elif val > 0:
            b = c
        else:
            a = c
    
    # Return the zero point
    return (a + b) / 2

# Test the function
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
This version of the `find_zero` function uses a binary search algorithm to find the zero point of the polynomial, which is more efficient than the original implementation using `math.pow`.