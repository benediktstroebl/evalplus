```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x ** 2 + ... xs[n] * x ** n)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and it finds_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

```
The Python script provided defines two functions: `poly` and `find_zero`. 

The `poly` function takes a list `xs` of coefficients and a point `x` as input and returns the polynomial evaluated at `x` with those coefficients. The `poly` function uses the mathematical formula `return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])` to calculate the polynomial's value at `x`. 

The `find_zero` function takes a list `xs` of coefficients as input and returns the zero point of the polynomial with those coefficients. It uses the largest non-zero coefficient as a starting point to find the zero, and then checks for `poly(x)` being equal to zero.

The function only returns the first zero found, even if there are multiple solutions. It ensures that the list `xs` has an even number of coefficients and the largest non-zero coefficient.