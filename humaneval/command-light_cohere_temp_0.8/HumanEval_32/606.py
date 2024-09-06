```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x such that polynomial (xs)(x) = 0.
    find_zero returns only zero point, even if there are many.
    """
    top degree coefficient guarantees a solution exists
    """
    return round(find_zero([1, 2]), 2)

# Test cases
xs = [1, 2]
xs = [-6, 11, -6, 1]
xs = [1, -1, 2]

result_1 = poly(xs, x)
result_2 = find_zero(xs)

print(f"The polynomial result at x={result_1} and {result_2} respectively:")
```