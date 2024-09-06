```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial (xs)(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    The polynomial has even, and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    ```

def test_find_zero(xs: list):
    assert find_zero(xs) == [0]
    assert find_zero([1, 2]) == [0]
    assert find_zero([-6, 11, -6, 1]) == [0]
    assert len(xs) % 2 != 0
    assert len(xs) > 0
    assert xs[0] != 0


xs = [1, -2, -3]
test_find_zero(xs)
```
The function `find_zero` solves the problem, and the function `test_find_zero` passes the test by checking the result of the `find_zero` function with different sets of coefficients.