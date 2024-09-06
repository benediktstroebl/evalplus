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
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many roots.
    # assert all coefficients are even, raises ValueError
    assert len(xs) == len(xs[0])
    assert xs[0] != 0
    assert xs[0] >= 0

    # find x such that xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n = 0
    x = -float('inf')
    while xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n > 0:
        x -= 1
    return x
```
The function `find_zero` takes a list `xs` as input, where `xs` are the coefficients of a polynomial. It returns the root of the polynomial p(x), where p(x) is equal to the polynomial evaluated at x, which is given by the function `poly`.