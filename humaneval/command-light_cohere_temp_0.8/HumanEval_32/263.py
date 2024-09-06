```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x only if there is exactly one solution
    """
    if len(xs) % 2 != 0:
        raise ValueError("find_zero only takes list xs having even number of coefficients")
    # use binary search to find x such that poly(x) = 0
    return xs[0] if xs[0] > 0 else xs[0] + x


# Test
print(poly([1, 2, -5])) # x^2 + 2x + 1 = 0
print(find_zero([1, 2, -5])) # x = 0
```