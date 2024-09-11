### Polynomial Evaluation and Zero Finding
#### A Python Script

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
    - xs (list): A list of coefficients of a polynomial in descending order of powers.
    - x (float): The point at which to evaluate the polynomial.

    Returns:
    - float: The value of the polynomial at point x.
    """
    return sum([coeff * (x ** i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of a polynomial with coefficients xs.

    Args:
    - xs (list): A list of coefficients of a polynomial with an even number of coefficients,
                 and the largest non-zero coefficient as the first element.

    Returns:
    - float: A zero of the polynomial.

    Notes:
    - This function uses the Babylonian method for finding roots of polynomials.
    - The function only returns one zero, even if there are multiple zeros.
    """
    if len(xs) % 2!= 0:
        raise ValueError("The list of coefficients must have an even number of elements.")

    n = len(xs) // 2
    c = xs[0]
    for i in range(n):
        c = c / (-xs[-1-i*2] / (i + 1))
    c *= xs[-1]
    # Newton's method for finding roots
    def f(x):
        return sum([coeff * (x ** i) for i, coeff in enumerate(xs)])
    def f_prime(x):
        return sum([i * coeff * (x ** (i - 1)) for i, coeff in enumerate(xs) if i > 0])

    x = 1
    while abs(f(x)) > 1e-10:
        x = x - f(x) / f_prime(x)

    return round(x, 2)


# Example usage:
print(find_zero([1, 2]))  # f(x) = 1 + 2x
print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script solves the given problem by implementing the `poly` function to evaluate a polynomial at a given point, and the `find_zero` function to find a zero of a polynomial. The `find_zero` function uses the Babylonian method for finding roots of polynomials. Note that the function only returns one zero, even if there are multiple zeros, and it only works for polynomials with an even number of coefficients and the largest non-zero coefficient as the first element.