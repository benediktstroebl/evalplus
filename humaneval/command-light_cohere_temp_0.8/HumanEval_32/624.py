```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0 + + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n]
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    finds x_zero in [0,1] using binary search.
    return x_zero
   
    -1

    # Test
    assert find_zero([1, 2]) == 0.0,
    assert find_zero([-6, 11, -6, 1]) == -1.0

    ```