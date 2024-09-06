```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that polynomial (xs)(x) = 0
    find_zero returns only zero point, even if there are many solutions.
    Moreover, find_zero only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2)  # returns (1 + 2x)
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # returns (-1+11x)+(-6x^2)+x^3
    -0.5
    ```
```

The `find_zero` function takes in a list `xs` which is a set of coefficients for a polynomial and returns the zero of this polynomial, `xs(x) = 0`. The function works by passing each element in the list `xs` to the `poly` function, which returns the result of evaluating the polynomial at x, which is the sum of the coefficients multiplied by the power of x. The function then iterates each element in `xs` through the list, and checks if the result is equal to 0. If the result is equal to 0, then the function returns the current element in `xs` as the zero of the polynomial. If the result is not equal to 0, then the function continues to the next element in `xs` until it finds an element that is equal to 0.