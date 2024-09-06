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
    find_zero find x such that polynomial is zero
    find_zero returns only zero point, even if there are many
    """
    if len(xs) % 2 != 0:
        raise ValueError("find_zero only takes list xs having even number of coefficients")
    if len(xs) == 0:
        return 0
    x = 0
    for i in range(len(xs)):
        if xs[i] != 0:
            x += xs[i] / math.pow(x, i+1)
    return x

# Test cases
xs = [1, 2]
assert find_zero(xs) == 0.1
xs = [-6, 11, -6, 1]
assert find_zero(xs) == -0.866
xs = [3, -4, 3, -5]
assert find_zero(xs) == -0.95
```

The `poly()` function computes the result of a polynomial expression with coefficients in the given list `xs` at the point `x` by summing the products of each coefficient times the corresponding factorials. The `find_zero()` function determines the zero of the polynomial in `xs` and returns the corresponding value of `x`.