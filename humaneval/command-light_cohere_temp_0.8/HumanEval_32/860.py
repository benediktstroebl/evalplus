```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.0] + + xs[n] * x^n + ... + xs[0]
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x and does so only if xs has even number of coefficients and the largest coefficient is not zero.

    if you need a can't find zero and returns None.
    >>> find_zero([1, 2]) # returns (0, 2)
    >>> find_zero([1, 2, 3]) # returns None
    """

def test(x: float):
    """
    test passes if x is a root of the polynomial
    """
    poly(xs=[1, 1, 1, 1, 1], x) == 0

xs = [1, 2]
x = find_zero(xs)
print(x) # returns 0 or None

test(x)
```