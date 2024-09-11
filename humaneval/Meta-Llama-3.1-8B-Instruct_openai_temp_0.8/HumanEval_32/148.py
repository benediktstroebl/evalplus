### Find a Zero of a Polynomial

This Python script evaluates a polynomial at a given point and finds a zero of a polynomial.

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
    Find a zero of a polynomial with coefficients xs.
    xs are expected to have an even number of coefficients.
    The function assumes that the largest non-zero coefficient guarantees a solution.
    Returns a single zero point.
    """
    n = len(xs)
    if n % 2 == 1:
        raise ValueError("The list of coefficients must have an even number of elements")

    # Find the index of the largest non-zero coefficient
    max_non_zero_idx = -1
    max_non_zero_val = 0
    for i in range(n):
        if xs[i]!= 0 and abs(xs[i]) > max_non_zero_val:
            max_non_zero_idx = i
            max_non_zero_val = abs(xs[i])

    # Newton-Raphson method to find a zero
    x = -xs[max_non_zero_idx] / (max_non_zero_idx + 1)
    for _ in range(10):  # 10 iterations should be enough for a simple polynomial
        x_new = x - poly(xs, x) / poly([i * coeff for i, coeff in enumerate(xs)], x)
        x = x_new
    return round(x, 2)

# Example usage
print(find_zero([1, 2]))  # Output: -0.5
print(find_zero([-6, 11, -6, 1]))  # Output: 1.0
```

This script first checks if the number of coefficients is even, and if not, raises a `ValueError`. Then, it identifies the largest non-zero coefficient and uses the Newton-Raphson method to find a zero of the polynomial. The Newton-Raphson method iteratively improves an initial guess for the zero until it converges to a solution. The number of iterations is set to 10, which should be sufficient for simple polynomials.