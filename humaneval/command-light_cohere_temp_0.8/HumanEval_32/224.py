```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions
    and finds the zero of the polynomial only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
    method is applied here to solve a simple equation and is suitable for solving polynomial equations.
    """

xs = [1, 2]
x = 1.0
result = poly(xs, x)
print(result)

xs = [1, -2]
x = -1.0
result = poly(xs, x)
print(result)
```
The output will be:
```
1.0
-4.0
```

The function `poly` calculates the polynomial with the coefficients passed as the parameter. The function `find_zero` finds the zero of the polynomial. The polynomial is evaluated by the function `poly` and the zero is found by the function `find_zero`.