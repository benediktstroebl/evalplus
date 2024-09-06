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
    find_zero finds x such that polynomial(x) = 0.
    find_zero returns only zero point, even if there are many.
    """
    find_zero only takes list xs having even number of coefficients and the largest non-zero coefficient as it guarantees a solution.
    return_list = [x for x in [x for x in xs if x != 0]] + [x for x in xs if x == 0]
    return_list
```
The `find_zero` function takes in a list `xs` of coefficients of a polynomial and returns the `x` value that makes the polynomial zero. The function works by first creating a new list `return_list` that contains all non-zero `x` values from the list `xs`, then it returns the `x` value at the end of this list.