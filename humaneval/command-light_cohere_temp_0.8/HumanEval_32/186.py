```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff ** math.pow(x) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial (xs)(x) = 0.
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    print(f(2.5))  # This print(f(1.5)) # prints 1.
    print(f(-1.0)) # prints 0.
    print(f(1.0)) # prints 0.0
    print(f(2.0)) # prints 0.
    print(f(-2.0)) # prints 0.0
    print(f(1.0)) # prints 0.0
    print(f(2.0)) # prints 0.
    print(f(-3.0)) # prints 0.0
    print(f(-4.0)) # prints 0.0
```


This script defines a function `poly` that evaluates a polynomial with coefficients in a list `xs` at a point `x`. It then defines a function `find_zero` that finds the zero of the polynomial in the list `xs` at a given `x`.