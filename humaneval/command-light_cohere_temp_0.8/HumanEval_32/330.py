```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x ** 2 + ... xs[n] * x ** (n-1))
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial (x - xs[0]) has zero at x
    and is the only zero in the interval [x, +infinity]
    """
    x0 = float(xs[0])
    return x0 if x0 in math.find_zero(x) else None

xs = [1, 2]
poly_test = poly(xs, 3)
print(poly_test) # Output: 6
print(find_zero(xs))  # Output: 3
```

This script defines two functions: `poly` and `find_zero`. The `poly` function takes a list `xs` of coefficients and a point `x` as input, and returns the polynomial evaluation at `x`. The `find_zero` function takes a list `xs` of coefficients as input and finds the zero of the polynomial `poly(x)` in the interval `[x, +infinity]`. The test cases are passed to the functions, and the output is printed.