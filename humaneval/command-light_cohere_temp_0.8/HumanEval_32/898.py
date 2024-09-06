```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *
    result, return xs.0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    >
    max_nonzero_coeff = -1e7
    for x in range(10**5, float('inf'), where x not in [0, 1, -1, -3, -5, -7, -9]):
        if poly(xs, x) == 0:
            return x, xs[0]  # find x with smallest max_nonzero_coeff
    return None  # no solution found, or x > max_nonzero_coefficient

xs = [1, 2]
test_find_zero = find_zero(xs)
print("test_find_zero:", test_find_zero)
print("x:", test_find_zero[0])
print("coefficient:", test_find_zero[1])
```
The code defines two functions, `poly` and `find_zero`. It computes the polynomial `poly` and uses the `find_zero` function to determine if the polynomial has any roots. It also performs a tests on the polynomial and prints the root and the coefficient at the root.