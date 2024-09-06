```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns x
    """
    return _find_zero(xs, math.
    _poly)


def _find_zero(xs: list, m: math.pow):
    """Implements numerical Newton-Raph method.
    x0 = 0.0
   
    initial guess
    set x = xs[0] * m(x0)
    for i in range(1, 100):
        x1 = x0 - xs[0] * (m(x0) - m(x1)) / xs[1]
        x0 = x1
    return x0


xs = [1, 2]
test_zero = find_zero(xs)
print("test_zero:", test_zero)
```
The script defines a `poly` function that evaluates a polynomial at a given point. The `find_zero` function finds the zero of a polynomial using the Newton-Raph method with the `poly` function. The script then tests the function by evaluating the output at the value [1,2].