```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.

    >, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    """
    above, if any coefficient is zero, it returns None.
    if len(xs) == 0:
        return None
    elif len(xs) == 1:
        return xs[0]
    elif len(xs) == 2:
        return math.sqrt(xs[0]) * math.pow(xs[1])
    else:
        return math.sqrt(xs[0]) * math.pow(xs[1]) / math.pow(xs[2])

# tests
xs = [1, 2]
print(find_zero(xs))
```