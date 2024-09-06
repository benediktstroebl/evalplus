```python
import math
def poly(xs: list, x: float) -> int:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])
def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial
    find_zero find x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    # Test case: make sure the list has even number of coefficients
    # check that largest non zero coefficient is not 0
    # this ensures that the polynomial has a root, and makes the subsequent code run faster
    if len(xs) % 2 != 0:
        raise ValueError("find_zero only takes even-length lists of coefficients")
    # sort the coefficients to make the process faster
    xs.sort_values = sorted(xs, reverse=True)
    # find the root of the polynomial
    x_root = -float('inf')
    while x_root <= float('inf') and poly(xs, x_root) != 0:
        x_root += 1
    return x_root
def test_find_zero():
    # create a list of coefficients
    xs = [1, 2]
    # test if the function returns the correct root
    x = find_zero(xs)
    assert x == 1.0
    # test return a done
```