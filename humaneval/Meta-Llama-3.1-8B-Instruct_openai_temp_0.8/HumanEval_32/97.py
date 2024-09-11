### Evaluating Polynomials and Finding Zeroes
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
    xs (list): List of coefficients of the polynomial.
    x (float): Point at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero of a polynomial.

    Args:
    xs (list): List of coefficients of the polynomial. The list must have an even number of coefficients,
               and the largest non-zero coefficient must be first.

    Returns:
    float: A zero of the polynomial.
    """
    if len(xs) % 2!= 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    if xs[0] == 0:
        raise ValueError("The largest non-zero coefficient must be first.")

    # Newton's method for finding a zero of a function
    def newton(f, df, x0, epsilon=1e-5, max_iter=100):
        x = x0
        for i in range(max_iter):
            x_next = x - f(x) / df(x)
            if abs(x_next - x) < epsilon:
                return x_next
            x = x_next
        return x

    # Define the polynomial and its derivative
    def f(x):
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    def df(x):
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

    return newton(f, df, x0=1)  # Initial guess of 1.

# Test the functions
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
This code uses Newton's method to find a zero of the polynomial. The `newton` function takes a function `f`, its derivative `df`, an initial guess `x0`, and some convergence parameters. The polynomial and its derivative are defined inside the `find_zero` function. The initial guess is set to 1, but you can change this if you have a better guess.

Note that the `find_zero` function raises an error if the list of coefficients does not have an even number of elements or if the largest non-zero coefficient is not first.