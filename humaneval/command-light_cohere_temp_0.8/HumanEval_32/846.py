```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns the first such x, even if there are many roots
    root = x0
    while not poly(xs) == 0:
        xs.append(x1 * root**xs**x)
        root = x0
    return root


xs = [1, 2]
poly_test = poly([xs], 3)
print(f"The polynomial is {poly_test}")
x_test = find_zero([xs])
print(f"The root of the polynomial is {x_test}")
```
The code defines two functions: `poly` and `find_zero`. The `poly` function evaluates a polynomial with coefficients passed as an argument and returns the polynomial result. The `find_zero` function finds the zero of the polynomial.