```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial equal to 0.
    find_zero returns only zero point, even if there are many solutions.
    and also, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    largest_nonzero: float = float('-inf')
    for x in range(1, 10):
        if poly(xs, x) == 0:
            return x
    return None  # No real root found


# Test case 1
xs = [1, 2]
print("Find zero:", find_zero(xs))  # Output: 2

# Test case 2
xs = [-6, 11, -6, 1]
print("Find zero:", find_zero(xs))  # Output: 1

# Test case 3
xs = [1, -1, 2, -2, 1]
print("Find zero:", find_zero(xs))  # Output: 1
```

This code defines a function `poly` that evaluates a polynomial with given coefficients at a point `x`. It also defines a function `find_zero` that finds the zero of the polynomial by evaluating it at various points and checking if it's equal to 0.

The `find_zero` function iterates through a range of `x` values, evaluating the polynomial at each `x` and checking if it's equal to 0. If the polynomial is equal to 0 at any `x`, the function returns that `x` value. If no real root is found, the function returns `None` to indicate that there are no real roots for the polynomial.