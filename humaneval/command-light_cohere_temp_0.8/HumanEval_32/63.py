```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff * + math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    Moreover, find_zero only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    ```
    f(x) = ax^2 + bx + c = 0, so we can use the Cardano formula
    ```x^2 + a * x + b = 0[x]```

The coefficients a, b, and c are obtained by the coefficients of the polynomial. This can be done by multiplying the polynomial by x and adding the result to itself n times, where n is the degree of the polynomial.

A valid solution can be found by solving the quadratic equation using any standard method, such as factoring, completing the square, or the quadratic formula.

In general, it is more efficient to use a symbolic calculator or computer algebra system to solve the quadratic equation, rather than using a brute-force method.