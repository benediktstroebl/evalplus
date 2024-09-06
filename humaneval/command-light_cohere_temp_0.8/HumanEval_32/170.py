```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x(s) only if there is exactly one solution.
    The, find_zero takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
   
    new test:
        - -0.5 * x + - + 11 * x^2 == -6 - 11x^3
        -6 * x + x^2 + x^3 == -11x^2 - 6x + x^2
        -6 + x^2 + x^3 - 11x^2 - 6x + x^2 == 0
    -11x^2 + x^2 - 6x + x^2 == 0
    -11x^2 + x^2 - 6x + x^2 - 1 == 0
    -1 * x^2 + x^2 - 6x + x^2 == 0
    1.0
    3.0* x^5
    game is to find the roots of a polynomial, so we need to solve a system of linear equations.

Problem: Given a list of coefficients xs representing a polynomial, find the roots of the polynomial.

```python
def poly(xs: list, x: float):
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x(s) only if there is exactly one solution.
    if len(xs) % 2 != 0:
        raise ValueError("Coefficients list must have even number of coefficients")
    l, r = len(xs), len(xs) // 2
    if xs[l] < xs[r]:
        l, r = r, l
    for i in range(l, r):
        if xs[i] == 0:
            return xs[i]
    return float('inf')

xs = [1, 2]
x = find_zero(xs)
print(x)
```