```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0, returns only zero point, even if there are many.
    """
   , finds_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    assert len(xs) % 2 == 0
    assert xs[0] != 0
    assert xs[-1] != 0

    x_low = xs[0] / xs[-1]
    x_high = 1 / xs[0]

    return x_low, x_high

xs = [1, 2]
x = find_zero(xs)
print("The root is ", x)
```
This Python script defines a function `poly` that evaluates a polynomial with given coefficients at a given point `x`. The function `find_zero` finds the zero of the polynomial `poly` and returns the corresponding value of `x`.