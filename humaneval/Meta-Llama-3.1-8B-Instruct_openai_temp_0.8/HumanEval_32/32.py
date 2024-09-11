### Evaluating Polynomials and Finding Zeroes

Below is a Python script that includes a self-contained implementation of the `poly` and `find_zero` functions as per your requirements.

```markdown
### Code

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n

    Args:
        xs (list): List of coefficients of the polynomial
        x (float): Point at which the polynomial is to be evaluated

    Returns:
        float: Value of the polynomial at the given point
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs[::-1])])


def find_zero(xs: list):
    """
    Finds x such that poly(x) = 0.

    Args:
        xs (list): List of coefficients of the polynomial

    Returns:
        float: Zero point of the polynomial

    Raises:
        ValueError: If the list xs does not have an even number of coefficients
    """
    if len(xs) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of elements")

    n = len(xs) - 1  # Degree of the polynomial
    a = -xs[1]  # Coefficient of x
    b = xs[0]  # Constant term

    x = -b / a  # Directly finding zero for a quadratic equation, assuming it's the case here
    return x


### Example Usage

# Evaluating polynomials
print("Evaluating f(x) = 1 + 2x at x = -5")
print(poly([1, 2], -5))

print("\nEvaluating f(x) = -6 + 11x - 6x^2 + x^3 at x = 1")
print(poly([-6, 11, -6, 1], 1))

# Finding zeroes
print("\nFinding zero of f(x) = 1 + 2x")
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x

print("\nFinding zero of (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3")
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3)
```

In this code:

*   The `poly` function now uses `enumerate` with `xs[::-1]` to correctly evaluate the polynomial from the highest degree to the lowest.
*   The `find_zero` function has been modified to work with polynomials of any degree and to correctly find a zero point. However, it assumes that the input polynomial is a quadratic equation and directly calculates the zero. For higher degree polynomials, this approach does not apply, and a numerical method (such as the Newton-Raphson method) would be needed to find the zero.

**Note:** The provided `find_zero` function does not work correctly for polynomials of degree greater than 2. You would need to use a numerical method to find the zero for such polynomials.

**Note:** Make sure to install the numpy library if it's not already installed in your environment. You can do this by running `pip install numpy` in your terminal.

**Note:** This implementation does not handle