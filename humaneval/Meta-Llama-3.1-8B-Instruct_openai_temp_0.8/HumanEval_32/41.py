### Polynomial Evaluation and Zero Finding
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
    xs (list): Coefficients of the polynomial in ascending order of powers.
    x (float): Point at which to evaluate the polynomial.

    Returns:
    float: Value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero point of a polynomial.

    Args:
    xs (list): Coefficients of the polynomial in ascending order of powers.

    Returns:
    float: A zero point of the polynomial.
    """
    if len(xs) % 2!= 0 or xs[-1] == 0:
        raise ValueError("Polynomial coefficients must have an even number of elements and the last coefficient must be non-zero")

    x = -xs[1] / (xs[0] + (xs[2] if len(xs) > 2 else 0))
    return x

# Example usage
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script first defines the `poly` function to evaluate a polynomial at a given point, and then defines the `find_zero` function to find a zero point of a polynomial. The `find_zero` function assumes that the input coefficients are in ascending order of powers and that the polynomial has an even number of coefficients with the last coefficient being non-zero. If these assumptions are not met, it raises a ValueError. In the example usage, it demonstrates finding zero points of two polynomials. 

Note: This is a simplified version of the `find_zero` function. In general, finding zero points of a polynomial can be a complex task and this function does not guarantee to find all zero points.