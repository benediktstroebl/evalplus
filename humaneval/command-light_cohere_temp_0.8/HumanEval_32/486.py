```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff * for coeff in xs])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that polynomial evaluated at x is 0, returns x
    """
    x = -math.floor(xs[0]) / math.floor(xs[1]) + 1
    return x

if __name__ == "__main__":
    print(poly([1, 2], 3))
    print(find_zero([1, 2]))
```