```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *f *math.pow(i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x, or None if no such x exists.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
   
    >>> round(find_zero([1, -1, -3]), 2) # f(x) = 1 + x^2 - 3x
    -1.0
    ```
``` 
The function `find_zero` is used to find the zero of a polynomial represented as a list of coefficients. It returns the x value that makes the polynomial equal to zero. The function works by evaluating the polynomial at the given x value and checking if the polynomial is equal to zero. It returns `x_` if the polynomial is equal to zero, and `None` if no such x exists.