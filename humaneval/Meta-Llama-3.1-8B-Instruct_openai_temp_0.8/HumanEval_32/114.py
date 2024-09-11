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
    Finds a zero of polynomial defined by coefficients in xs.
    
    Args:
    xs (list): Coefficients of a polynomial in descending order.
    
    Returns:
    float: A zero of the polynomial.
    """
    if len(xs) % 2!= 0:
        raise ValueError("List xs must have an even number of coefficients")
    
    n = len(xs)
    
    # Initialize a and b for the bisection method
    a = 0
    b = 2 if xs[0] > 0 else -2
    
    # Perform the bisection method
    while abs(b - a) > 0.0001:
        c = (a + b) / 2
        f_c = xs[0]
        for i in range(1, n):
            f_c += xs[i] * math.pow(c, i)
        if f_c > 0:
            b = c
        else:
            a = c
            
    return round((a + b) / 2, 2)

# Test the function
print(find_zero([1, 2]))  # f(x) = 1 + 2x
print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Please note that this code utilizes the bisection method to approximate a zero of the polynomial. This method works by repeatedly dividing the interval in half and selecting the half that contains the root. The method stops when the interval is small enough (i.e., the difference between the two ends of the interval is less than 0.0001). 

This code is a modified version of the given code block. It includes error handling for the case when the input list `xs` does not have an even number of coefficients.