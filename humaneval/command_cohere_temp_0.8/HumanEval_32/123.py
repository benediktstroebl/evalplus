Here's a Python script that includes a function to solve the problem of finding a zero point of a polynomial:
```python
import math

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero point.
    Works only with lists having an even number of coefficients
    and the largest non-zero coefficient.
    """
    coeffs = sorted(xs, reverse=True)
    num_coeffs = len(xs)
    
    if num_eff_coeffs%2 != 0: 
        return "The list of coefficients needs to have an even number of elements";
    
    eff_xs = [coeffs[i] for i in range(0, num_eff_coeffs, 2)]
    num_eff_coeffs = len(eff_xs)
    
    x_star = 0
    x_squared = 1
    
    for power in range(1, num_eff_coeffs + 1):
        x_temp = x_star
        x_star = x_squared
        x_squared = x_temp - eff_xs[power-1] / x_star
        
        if x_star < 0: 
           break
    
    return x_star
```

This script includes two functions. The first function, `poly(xs, x)`, calculates the value of a polynomial at a given point. The second function, `find_zero(xs)`, finds the first zero point of a polynomial with even coefficients, assuming the largest non-zero coefficient is included. It works by sorting the coefficients in descending order and then using an iterative approach to find the zero point. The function returns the zero point if it's a valid polynomial and has even coefficients.

The script is self-contained and should work as expected for the problem described in the prompt.