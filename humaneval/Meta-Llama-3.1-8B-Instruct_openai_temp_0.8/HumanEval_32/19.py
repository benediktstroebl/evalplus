### Polynomial Evaluation and Zero Finding

Below is the Python script that implements the polynomial evaluation and zero finding functions.

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Parameters:
    xs (list): List of coefficients in descending order of powers.
    x (float): Point at which the polynomial is evaluated.

    Returns:
    float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs[::-1])])

def find_zero(xs: list):
    """
    Finds a zero of a polynomial given its coefficients.

    Parameters:
    xs (list): List of coefficients in descending order of powers, must have an even number of coefficients.

    Returns:
    float: A zero of the polynomial. If no solution exists, returns None.
    """
    if len(xs) % 2!= 0 or not all(coeff == 0 for coeff in xs[:-1]):
        raise ValueError("List of coefficients must have an even number and the largest non-zero coefficient.")

    n = len(xs) // 2  # Degree of the polynomial
    p = np.poly1d(xs[::-1])

    # Find a root using the quadratic formula
    a, b, c = p.coefficients
    d = b**2 - 4*a*c
    if d < 0:
        return None  # No real solutions
    elif d == 0:
        return -b / (2*a)
    else:
        return (-b + np.sqrt(d)) / (2*a)


# Test cases
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    try:
        print(find_zero([1, 2, 3]))  # Invalid input
    except ValueError as e:
        print(e)
    try:
        print(find_zero([1]))  # No solution
    except ValueError as e:
        print(e)
```

Note that the `find_zero` function now uses the `numpy` library to create a polynomial from the coefficients and then finds a root using the quadratic formula. This function raises a `ValueError` if the input list of coefficients is invalid. The test cases have been updated to reflect the new implementation.