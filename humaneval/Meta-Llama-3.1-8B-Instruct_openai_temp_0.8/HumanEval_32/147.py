Here's a self-contained Python script that solves the problem using the Rational Root Theorem to find at least one zero of a polynomial:
```markdown
### Polynomial Zero Finder

This script uses the Rational Root Theorem to find at least one zero of a polynomial.

#### Code

```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Find x such that poly(x) = 0 using the Rational Root Theorem.

    Args:
    xs (list): coefficients of a polynomial.

    Returns:
    float: at least one zero of the polynomial.

    Raises:
    TypeError: If the input is not a list.
    """
    if not isinstance(xs, list):
        raise TypeError("Input must be a list.")

    if len(xs) % 2!= 0:
        raise ValueError("Input list must have an even number of coefficients.")

    # Find possible rational roots using the Rational Root Theorem
    factors = set()
    for i in range(1, int(math.sqrt(xs[-1])) + 1):
        if xs[-1] % i == 0:
            factors.add(i)
            factors.add(-i)
            factors.add(xs[-1] // i)
            factors.add(-xs[-1] // i)
    factors = sorted(factors)

    # Test possible rational roots
    for factor in factors:
        if poly(xs, factor) == 0:
            return factor

    # If no rational root is found, return a floating point approximation
    return round(poly(xs, 1.0) / poly(xs, 1.0, 1), 5)

def poly_derivative(xs: list, x: float):
    """
    Evaluates derivative of polynomial with coefficients xs at point x.
    return xs[1] + xs[2] * 2x +.... xs[n] * (n-1)x^(n-2)
    """
    return sum([coeff * (i) * math.pow(x, i-1) for i, coeff in enumerate(xs)])

def find_zero_secant(xs: list, x0: float, x1: float, tolerance: float = 0.0001, max_iter: int = 1000):
    """
    Find x such that poly(x) = 0 using the secant method.

    Args:
    xs (list): coefficients of a polynomial.
    x0 (float): initial guess.
    x1 (float): second initial guess.
    tolerance (float, optional): tolerance for convergence. Defaults to 0.0001.
    max_iter (int, optional): maximum number of iterations. Defaults to 1000.

    Returns:
    float: at least one zero of the polynomial.
    """
    for _ in range(max_iter):
        x2 = x1 - poly(xs, x1) * (x1 - x0) / (poly(xs, x1) - poly(xs, x0))
        if abs(poly(xs, x2)) < tolerance:
            return x2
        x0 = x1
        x1 = x2
    return x1

if __name__ == "__main__":
    # Test the find_zero function
    print(find_zero([1, 2]))  # f(x) = 1 + 2x
    print(find_zero([-6, 11, -6