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
    find_zero find x such that poly(x) = 0
    find_zero returns x and poly(x) = 0
    """
    x = -math.log(math.e)
    template x for calculating log(b)
    while True:
        x = x + 1
        if poly(xs, x) == 0:
            return x, poly(x)
    return None, None

# test
xs = [1, 2]
x = find_zero(xs)
print(x, xs)  # x = 1, xs = [1, 2]

xs = [-6, 11, -6, 1]
x, ans = find_zero(xs)
if x is not None:
    print(x, ans)
    assert x == -math.e
    assert ans == 1

```