```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    """
    if len(xs) == 1:
        return 0
    if len(xs) % 2 != 0:
        raise ValueError("find_zero only takes list of even length")
    return find_zero_impl(xs)

def find_zero_impl(xs: list):
    """
    x = 0
    lmb = xs[0]
    for x in range(1, float(len(xs))):
        if poly(xs, x) == 0:
            lmb = max(lmb, xs[x])
    return x
```
The above code defines a function `poly` that computes the value of a polynomial with coefficients given in `xs` at `x`. The `find_zero` function takes a list of coefficients `xs` as input and finds the zero of the polynomial with those coefficients at `x`. The `find_zero_impl` function is a helper function that finds the zero of the polynomial by comparing the polynomial's value to zero at various `x` values and returning the `x` value that results in a zero.