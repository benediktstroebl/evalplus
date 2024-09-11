```python
import math
import numpy as np


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n

    Args:
    xs (list): Coefficients of the polynomial, from lowest degree to highest
    x (float): Point to evaluate the polynomial at

    Returns:
    float: The value of the polynomial at point x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs[::-1])])


def find_zero(xs: list):
    """
    Finds a zero of a polynomial given its coefficients.

    Args:
    xs (list): Coefficients of the polynomial, from lowest degree to highest.
               The length of xs must be even.

    Returns:
    float: A value of x such that poly(x) = 0

    Raises:
    ValueError: If the length of xs is odd or the largest coefficient is zero
    """
    if len(xs) % 2!= 0 or xs[0] == 0:
        raise ValueError("xs must have an even number of coefficients and its largest coefficient must be non-zero")

    # Use numpy to find the roots of the polynomial, which are the zeros of the equation
    roots = np.roots(xs[::-1])

    # The problem statement asks for a single zero, so we take the first one
    return round(float(roots[0]), 2)


# Example usage
if __name__ == "__main__":
    print(find_zero([1, 2]))  # f(x) = 1 + 2x
    print(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```