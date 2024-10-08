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
    find_zero finds x such that poly(x) = 0,
    finds only one zero, even if there are many.
    The solution guarantees that there is exactly one root and it is the only root.
    we find the simplest form for poly(x), which is:
    xs = [1, x, x**2, ... x**n]
    if xs[0] != 1:
        return None
    if xs[0] == 1:
        return [x]
    else:
        return [x] + find_zero([xs[1], xs[2], ...])
```