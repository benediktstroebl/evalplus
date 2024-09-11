### Newton-Raphson Method for Finding Polynomial Roots

This script utilizes the Newton-Raphson method for finding roots of a polynomial. The Newton-Raphson method iteratively finds the roots of a function by using the formula:

    f(x_n+1) = f(x_n) - f'(x_n)/(f'(x_n))

where `x_n` is the current estimate of the root, `f'(x_n)` is the derivative of the function at `x_n`, and `x_n+1` is the new estimate of the root.

```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def derivative_poly(xs: list, x: float):
    """
    Evaluates derivative of polynomial with coefficients xs at point x.
    return xs[1] + 2*xs[2]*x + 3*xs[3]*x^2 +.... n*xs[n]*x^(n-1)
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

def newton_raphson(xs: list, x0: float, max_iter: int = 100, tol: float = 1e-5):
    """
    Finds root of polynomial with coefficients xs using Newton-Raphson method.

    Args:
        xs (list): Coefficients of the polynomial.
        x0 (float): Initial guess for the root.
        max_iter (int, optional): Maximum number of iterations. Defaults to 100.
        tol (float, optional): Tolerance for convergence. Defaults to 1e-5.

    Returns:
        float: The root of the polynomial.
    """
    x = x0
    for _ in range(max_iter):
        f = poly(xs, x)
        if math.isclose(f, 0, rel_tol=tol):
            return x
        f_prime = derivative_poly(xs, x)
        if math.isclose(f_prime, 0, rel_tol=tol):
            raise ValueError("Derivative is zero at x = {}".format(x))
        x = x - f / f_prime
    raise RuntimeError("Failed to converge after {} iterations".format(max_iter))

def find_zero(xs: list):
    """
    Finds root of polynomial with coefficients xs.

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        float: The root of the polynomial.
    """
    if len(xs) % 2!= 0:
        raise ValueError("Number of coefficients must be even")
    if xs[-1] == 0:
        raise ValueError("Largest non-zero coefficient must be last")
    return newton_raphson(xs, 1)

# Test the functions
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script first defines the `poly` function to evaluate a polynomial at a given point, and the `derivative_poly` function to evaluate the derivative of a polynomial at a given point. The `new