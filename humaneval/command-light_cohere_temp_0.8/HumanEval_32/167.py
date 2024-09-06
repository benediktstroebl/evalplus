```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes the polynomial equal to 0, returns only zero point, even if there are many roots.
    """
    root = - root = 0
    for x in range(-20, 20):
        polynomial = xs[0] + xs[1] * x + xs[2] * x**2 + ... + xs[-1] * x**(-1)
        if polynomial == 0:
            root = x
    return root


def test_find_zero(xs: list):
    """ Test the find_zero function
    assert find_zero([1, 2]) == 0
    assert find_zero([-6, 11, -6, 1]) == 1.0
    assert find_zero([2, 3, 2, -1]) == -2.0


print(poly([1, 2, -3]))  # print polynomial
print(find_zero([1, 2, -3]))  # print zero of polynomial
```