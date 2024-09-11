### Zero Finder for Polynomials
```python
import math
from scipy.optimize import fsolve

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    - xs (list): A list of coefficients of the polynomial.
    - x (float): The point at which to evaluate the polynomial.
    
    Returns:
    - The value of the polynomial at x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero point of a polynomial given its coefficients.
    
    Args:
    - xs (list): A list of coefficients of the polynomial. The list must have an even number of elements.
    
    Returns:
    - A zero point of the polynomial.
    """
    if len(xs) % 2 == 1:
        raise ValueError("Polynomial must have an even number of coefficients")
    
    def func(x):
        return poly(xs, x)
    
    # Use fsolve to find a zero point of the polynomial
    return fsolve(func, 0)[0]


# Test the function
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
This script uses the `fsolve` function from the `scipy.optimize` module to find a zero point of the polynomial. The `fsolve` function takes a function and an initial guess for the solution, and returns the solution. In this case, the function is the `poly` function, and the initial guess is 0.

Note that the `fsolve` function may not always find the exact zero point of the polynomial, especially if the polynomial has multiple zeros or the `fsolve` function is not able to converge to the solution. However, it should be able to find a reasonable approximation for most polynomials.