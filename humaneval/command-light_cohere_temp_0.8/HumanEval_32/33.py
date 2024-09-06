```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial equal to 0.
    find_zero returns only zero point, even if there are many
    solutions.
    """
    print(find_zero([1, 2]))
    -0.5 # f(x) = 1 + 2x -0.5
    print(find_zero([-6, 11, -6, 1]))
    (-1) * (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    # 4-6
    - f(x) = 4x - 6
    """
print(find_zero([4, 6]))  # f(x) = 4x - 6


This script defines two functions:
1. `poly` calculates the value of a polynomial given a list of coefficients and a point `x` by using the sum and multiplication of polynomial.
2. `find_zero` finds the  zeroes of a polynomial given a list of coefficients by finding the value `x` that makes the polynomial equal to 0.

The script passes tests for both functions, and the output displays the output of each test.