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
    find_zero returns only zero point, even if there are many.
    It, moreover, finds_zero only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    print("The solution is ", round(x,2)) for x in find_zero([1,2]))
    ```

This script defines a function `poly` that evaluates a polynomial with coefficients provided as a list at a given point `x`. The function returns the polynomial's value at `x`. The function `find_zero` finds the zero of the polynomial with coefficients provided as a list, it returns the `x` value that makes the polynomial equal to zero.