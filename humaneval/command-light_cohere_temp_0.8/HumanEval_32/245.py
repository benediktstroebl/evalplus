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
    find_zero find x such that poly(x) = 0,
    returns x and value at x
    """
    x = float('inf')
    val = float('-inf')
    while x != 0:
        x = (-x) / math.poly(xs[0])
        val = xs[0] * x - sum([xs[i] * math.pow(x, i) for i in range(1, len(xs)))]
    return x, val

xs = [1, 2]
print(find_zero(xs))
```
This script defines a function `poly` that evaluates a polynomial at a given point `x` based on its coefficients `xs`. The `find_zero` function finds the root of the polynomial `poly(x)` equals zero, and returns the value of `x` at which the polynomial evaluates zero. The script then calls the for the given coefficients `[1, 2]` and prints the result.