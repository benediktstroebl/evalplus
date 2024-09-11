### Polynomial Evaluation and Zero Finding
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n

    Args:
        xs (list): A list of coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.

    Returns:
        float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a root of a polynomial with coefficients xs.
    Finds a zero point, even if there are many.
    xs are coefficients of a polynomial and must have even number of coefficients.
    Largest non-zero coefficient guarantees a solution.

    Args:
        xs (list): A list of coefficients of the polynomial.

    Returns:
        float: A zero point of the polynomial.
    """
    # Check if the list has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("List xs must have an even number of coefficients")

    # Find the index of the largest non-zero coefficient
    max_idx = np.argmax([abs(coeff) for coeff in xs if coeff!= 0])

    # Evaluate the polynomial at the point where the largest non-zero coefficient is zero
    x = -xs[max_idx + 1] / xs[max_idx]
    return x

# Test cases
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
This script defines two functions: `poly` for evaluating a polynomial at a given point, and `find_zero` for finding a root of a polynomial. The `poly` function uses a list of coefficients and an evaluation point to compute the polynomial's value. The `find_zero` function takes a list of coefficients, finds the index of the largest non-zero coefficient, and evaluates the polynomial at the point where this coefficient is zero. It returns this zero point. The script includes test cases to demonstrate the functions' usage.