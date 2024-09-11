Here's the Python script that solves the problem:

```markdown
### Evaluating Polynomials and Finding Zero Points

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
    xs (list): A list of coefficients of the polynomial.
    x (float): The point at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial represented by its coefficients.

    Args:
    xs (list): A list of coefficients of the polynomial.
        The list must have an even number of elements and the largest non-zero coefficient must be at the end.

    Returns:
    float: A zero point of the polynomial.
    """
    n = len(xs)
    if n % 2!= 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    
    # Check if the largest non-zero coefficient is at the end
    if max(xs[:-1])!= 0:
        raise ValueError("The largest non-zero coefficient must be at the end.")

    # Find the zero point using the formula for the x-coordinate of the centroid of a polynomial
    return -xs[1] / (xs[0] + (n - 1) * xs[2])

# Test the functions
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
In this code, the `find_zero` function uses a formula to find a zero point of a polynomial. This formula is a simplified version of the formula for the x-coordinate of the centroid of a polynomial.

However, this approach will only work for certain types of polynomials. A more general approach to find the roots of a polynomial would be to use numerical methods such as the Newton-Raphson method or a library function like `numpy.roots`.

Here's how you might implement the Newton-Raphson method for finding roots of a polynomial:

```markdown
### Newthon-Raphson Method for Finding Roots of a Polynomial

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
    xs (list): A list of coefficients of the polynomial.
    x (float): The point at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def poly_derivative(xs: list, x: float):
    """
    Evaluates the derivative of the polynomial with coefficients xs at point x.

    Args:
    xs (list): A list of coefficients of the polynomial.
    x (float): The point at which to evaluate the derivative.

    Returns:
    float: The value of the derivative at point x.
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs)])

def newton_raphson(xs: list, x0: float, max_iter: int = 1000, tol: float = 1e