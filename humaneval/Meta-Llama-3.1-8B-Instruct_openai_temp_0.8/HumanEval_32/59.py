### Newton-Raphson Method for Finding a Zero of a Polynomial

The following Python script uses the Newton-Raphson method to find a zero of a polynomial. This method is an iterative process that refines an initial estimate of the zero until it converges to the actual value.

```markdown
### Code
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
        xs (list): Coefficients of the polynomial in ascending order of exponents.
        x (float): Point at which to evaluate the polynomial.

    Returns:
        float: Value of the polynomial at point x.
    """
    return sum([coeff * x**i for i, coeff in enumerate(xs)])

def derivative(xs: list, x: float):
    """
    Evaluates the derivative of the polynomial at point x.

    Args:
        xs (list): Coefficients of the polynomial in ascending order of exponents.
        x (float): Point at which to evaluate the derivative.

    Returns:
        float: Value of the derivative at point x.
    """
    return sum([i * coeff * x**i for i, coeff in enumerate(xs)])

def find_zero(xs: list, initial_guess: float = 1.0, tolerance: float = 1e-5, max_iter: int = 100):
    """
    Finds a zero of the polynomial using the Newton-Raphson method.

    Args:
        xs (list): Coefficients of the polynomial in ascending order of exponents.
        initial_guess (float): Initial estimate of the zero. Defaults to 1.0.
        tolerance (float): Maximum difference between consecutive estimates of the zero. Defaults to 1e-5.
        max_iter (int): Maximum number of iterations. Defaults to 100.

    Returns:
        float: Zero of the polynomial.
    """
    x = initial_guess
    for _ in range(max_iter):
        x_next = x - poly(xs, x) / derivative(xs, x)
        if abs(x_next - x) < tolerance:
            return x_next
        x = x_next
    return x

# Test the function
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

### Explanation

The script defines three functions:

1.  `poly(xs, x)`: Evaluates the polynomial at point `x` with coefficients `xs`.
2.  `derivative(xs, x)`: Evaluates the derivative of the polynomial at point `x` with coefficients `xs`.
3.  `find_zero(xs, initial_guess, tolerance, max_iter)`: Finds a zero of the polynomial using the Newton-Raphson method.

The `find_zero` function takes the coefficients of the polynomial `xs`, an initial estimate of the zero `initial_guess`, a tolerance for convergence `tolerance`, and a maximum number of iterations `max_iter`. It iteratively refines the estimate of the zero until it converges to the actual value within the specified tolerance or reaches the maximum number of iterations.

The script includes test cases to demonstrate the usage of the `find_zero` function.