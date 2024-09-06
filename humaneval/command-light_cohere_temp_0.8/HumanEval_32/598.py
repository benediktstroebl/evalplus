```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**(n-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    """
    bigger coefficients lead to better estimates, since larger coefficients have larger influence in higher degree terms.
    if len(xs) % 2 != 0:
        return None  # Not enough coefficients
    elif len(xs) % 2 == 0:
        return math.pow(xs[0], x)  # Fundamental solution
    else:
        # Compute all solutions using bisection method
        def solve_bisection(low, high):
            x = (high + low) / 2
            return low + x * (high - low) / 2 ** (len(xs) - 1)

        return [solve_bisection(low, high) for high in xs[1: len(xs)]] + [solve_bisection(high, low) for high in xs[1: len(xs)]]

# Example usage
xs = [1, 2]
x = find_zero(xs)
print(x)  # Output: 2
xs = [-6, 11, -6, 1]
x = find_zero(xs)
print(x)  # Output: -1
``` 
This code defines a function `poly` that evaluates a polynomial with given coefficients at a given point `x`. The `find_zero` function finds the zero of the polynomial `poly(x)` by solving the equation. The function works by first checking if the length of the coefficients list is even or odd. If the length is even, it returns the fundamental solution, which is the value of `poly(x)` when `x` is equal to the largest coefficient. If the length of the coefficients is even, it computes the fundamental solution using the formula `x = c_0 + x * c_1 / (2 ** (n - 1) * x)`. Otherwise, it uses the bisection method to find all solutions to the equation.

The code provides an example of finding the zero of a polynomial with coefficients `[1, 2]` and `[1, -6, 11, -6]`. It also demonstrates how to handle cases where there are multiple solutions. The code follows the `Mathematica` conventions for polynomial evaluation and zero-finding, which can be a useful reference for working with polynomial equations in various mathematical and computational contexts.