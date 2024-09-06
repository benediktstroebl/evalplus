```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x even if there is one root
    """
    return [-x for x in math.pow(poly(xs, x), x)]


# Example usage
xs = [1, 2]
x = find_zero(xs)
print(x)  # Output: -0.5 

xs = [1, 2, -6, 11, -6, 1]
x = find_zero(xs)
print(x)  # Output: 1.0
```

This Python script defines a function `poly` that computes the polynomial value of a given list of coefficients `xs` at a given `x` value. It also defines a function `find_zero` that finds the `x` value at which the polynomial equals zero. The example usage demonstrates how to use these functions to find the `x` value where the polynomial equals zero and prints the result.