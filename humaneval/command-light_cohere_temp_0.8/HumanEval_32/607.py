```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *x + math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x and polynomial division by x
    """
    return [x] if x != 1 else None


# Test
xs = [1, 2]
x = 0.0
result = poly(xs, x)
result = result - xs[0]  # True
result = result - xs[1]  # True
result = result - math.pow(x, 0.0)  # True
print("result =", result)

zero = find_zero([1, 2])
zero = zero[0]  # True
print("zero =", zero)
```