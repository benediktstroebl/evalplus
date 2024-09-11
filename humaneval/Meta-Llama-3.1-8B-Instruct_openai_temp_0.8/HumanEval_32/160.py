### Polynomial Evaluation and Root Finding
```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n

    Args:
        xs (list): A list of coefficients of the polynomial, in ascending order of powers.
        x (float): The point at which to evaluate the polynomial.

    Returns:
        float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, degree) for degree, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a root of a polynomial with coefficients xs.

    Args:
        xs (list): A list of coefficients of the polynomial, in ascending order of powers.

    Returns:
        float: A root of the polynomial, rounded to 2 decimal places.

    Raises:
        ValueError: If the input list does not have an even number of coefficients.
    """
    if len(xs) % 2!= 0:
        raise ValueError("Input list must have an even number of coefficients")

    # Find the root by solving the polynomial equation
    # We use a simple iterative approach to find a root
    x = 1.0
    precision = 0.00001
    while True:
        f_x = poly(xs, x)
        f_x_prime = poly([i * coeff for i, coeff in enumerate(xs[1:], 1)], x)
        if abs(f_x_prime) < precision:
            break
        x -= f_x / f_x_prime
        if abs(f_x) < precision:
            break

    return round(x, 2)


# Test cases
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    try:
        print(find_zero([1, 2, 3]))  # Test case with an odd number of coefficients
    except ValueError as e:
        print(e)
```
This script defines two functions: `poly` for evaluating a polynomial at a given point, and `find_zero` for finding a root of a polynomial. The `find_zero` function uses a simple iterative approach to find a root, and raises a `ValueError` if the input list does not have an even number of coefficients. The script includes test cases to demonstrate the functionality of the `find_zero` function.