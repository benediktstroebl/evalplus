```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that satisfies polynomial equation 0 = f(x) with coefficients xs
    """
    return round(find_zero_(xs), 2)

def find_zero_(xs: list):
    """
    Find a zero for polynomial with coefficients xs
    f(x) = sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])
    i = len(xs) - 1
    while True:
        a = i - 1
        b = xs[a] / math.pow(xs[i], x)
        if b == 0:
            return x
        i -= 1
    """

# Example usage
xs = [1, 2]
x = find_zero(xs)
print(f"{x} is a root of the polynomial")
```

This script defines a function that takes a list of coefficients and a point `x` as input, and returns the value of the polynomial at `x`. The function then uses the Newton-Raph method to find the root of the polynomial, and prints out the root of the polynomial.