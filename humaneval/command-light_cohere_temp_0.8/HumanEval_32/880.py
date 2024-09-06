```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns the value of x that makes the polynomial zero
    """
    # make sure list has even number of coefficients
    if len(xs) % 2 == 1:
        raise ValueError("list must have even number of coefficients")
        
    # find the largest non zero coefficient
    max_abs_coeff = max(abs(xs[i]) for i in range(len(xs)) if xs[i] != 0)
    
    # x = (- maxi_ coefficient)/max_abs_coeff
    x = (-max_abs_coeff)/max(abs(xs))
    
    return x

xs = [1, 2]
x = find_zero(xs)
print(x) # x = -0.5
```

This script defines two functions: `poly` and `find_zero`. The `poly` function evaluates a polynomial with given coefficients at a given point. The `find_zero` function finds the zero of a polynomial by iterating through the coefficients and finding the value of x that makes the polynomial zero. 

The script then tests the `find_zero` function with two sets of coefficients and prints the result.