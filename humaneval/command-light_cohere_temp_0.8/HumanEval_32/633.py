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
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

    ```
```

The code has a function called `find_zero` that takes a list of coefficients `xs` and returns the zero value for the polynomial `poly(x)`. The function works by finding the zero value of the polynomial function using the `poly` function, and then returns the value of the polynomial evaluated at the zero point. 

The function also only returns the zero point, even if there are multiple solutions. This is guaranteed by taking coefficients with even number and having the largest non-zero coefficient, which ensures there's always a solution.

The test cases are also self-contained, as the function `find_zero` is called with a list of coefficients and the result is printed.