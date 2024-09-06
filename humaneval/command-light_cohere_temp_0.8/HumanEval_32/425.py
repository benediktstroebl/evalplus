```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x in xrange if x is zero.
    find_zero returns only zero point, even if there are many solutions
    and it takes list xs having even number of coefficients.
    and largest non zero coefficient as it guarantees a solution.
    xrange = [0, 1/x1, ..., -1/x1**2, ..., -1]
    x = 0
    while x not in xrange:
        if poly(xs, x) == 0:
            return x
    x += 1
    return None

xs = [1, 2]
x = find_zero(xs)
print(x) # 1
print(poly(xs, x)) # 1 + 2x
```