```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial(x) = 0
    find_zero returns only zero point, even if there are many.
    and find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    # test case:
    assert(poly(xs, x) == 0), assert(find_zero([1, 2]) == 1.0)
   
    output:
    x

# evaluation test:
    assert(poly(xs[:10], x) == 0), assert(find_zero([1, 2, 3, 4, 5, 6, 7, 8])) == 6.0
    # f(x) = 1 + 2x -3.5 + 4x2 *
    > 0, <1.1
    -0.5
```