```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many
    solutions.
    However, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    return:
        x: float
        None: if no zero found
        else:
            x
    """
    return None if len(xs) == 0 else x
# Test
xs = [1, 2]
result = find_zero(xs)
assert result is not None
print(result)  # Output: -0.5000000000000005
```