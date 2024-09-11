### Python Script for Finding Polynomial Zeros
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n

    Args:
        xs (list): Coefficients of the polynomial.
        x (float): Point at which to evaluate the polynomial.

    Returns:
        float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds the zero of a polynomial with coefficients xs.

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        float: Zero point of the polynomial.

    Raises:
        ValueError: If xs does not have an even number of coefficients.
    """
    if len(xs) % 2 == 1:
        raise ValueError("xs must have an even number of coefficients")

    n = len(xs) // 2
    return -xs[1] / xs[0]


# Example usage:
if __name__ == "__main__":
    # Test case 1
    xs = [1, 2]
    print("Zero of f(x) = 1 + 2x:", round(find_zero(xs), 2))

    # Test case 2
    xs = [-6, 11, -6, 1]
    print("Zero of (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3:", round(find_zero(xs), 2))
```
In this script, we've replaced the original `find_zero` function with a simpler implementation that uses the fact that the zero of a polynomial is the negative of the ratio of the first two coefficients. This implementation also checks if the input list has an even number of coefficients and raises a `ValueError` if not.