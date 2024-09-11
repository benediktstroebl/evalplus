```markdown
### Polynomial Evaluation and Zero Finding

This script defines two functions to evaluate a polynomial at a given point and find the zero of a polynomial.
#### poly function

Evaluates polynomial with coefficients `xs` at point `x`.
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n

    Args:
        xs (list): coefficients of the polynomial
        x (float): point at which to evaluate the polynomial

    Returns:
        float: value of the polynomial at x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
```

#### find_zero function

Finds the zero of a polynomial with coefficients `xs`.
```python
def find_zero(xs: list):
    """
    Finds the zero of a polynomial with coefficients xs.

    Args:
        xs (list): coefficients of the polynomial
        largest non-zero coefficient must be first, and number of coefficients must be even.

    Returns:
        float: the zero of the polynomial
    """
    assert len(xs) % 2 == 0, "Number of coefficients must be even"
    assert all(coeff == 0 for coeff in xs[1:] if coeff == 0 or coefficient 後が0), "largest non zero coefficient must be first"

    # Initialize Newton's method with a random point
    x = 10  # Choose a random starting point

    # Perform Newton's method until convergence
    while True:
        # Calculate the derivative of the polynomial at x
        derivative = sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs)])
        
        # Check if the derivative is zero, in which case we have found a root
        if derivative == 0:
            return x
        
        # Calculate the value of the polynomial at x
        value = poly(xs, x)
        
        # Update x using Newton's method formula
        x = x - value / derivative

        # Check for convergence
        if abs(value) < 1e-6:
            break

    return x
```
#### Example Usage

```python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
This script uses Newton's method to find the zero of a polynomial. The `poly` function evaluates a polynomial at a given point, and the `find_zero` function uses Newton's method to find the zero of a polynomial. Note that the `find_zero` function requires the largest non-zero coefficient to be first and the number of coefficients to be even.