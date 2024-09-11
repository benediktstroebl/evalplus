### Evaluating Polynomial and Finding Zero Point

Below is a Python script that defines a function to evaluate a polynomial and another function to find a zero point of the polynomial.

```python
import math
import numpy as np
from scipy.optimize import fsolve

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Find x such that poly(x) = 0 using fsolve from scipy.
    xs are coefficients of a polynomial.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Ensure the input list has an even number of coefficients
    assert len(xs) % 2 == 0, "List xs must have an even number of coefficients"
    
    # Define a function to find the zero point of the polynomial
    def func(x):
        return poly(xs, x)
    
    # Use fsolve to find the zero point
    x0 = -xs[1] / xs[0]  # initial guess
    zero = fsolve(func, x0)[0]
    
    return round(zero, 2)

# Test the functions
print(find_zero([1, 2]))  # f(x) = 1 + 2x
print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note that the `fsolve` function from `scipy.optimize` is used to find the zero point of the polynomial. The initial guess `x0` is set to `-xs[1] / xs[0]`, which is a reasonable choice for polynomials with an even number of coefficients.