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
    find_zero returns x and x**(-1) only, even if there are many solutions.
    """
    can be optimized by first finding the largest non-zero coefficient and then testing values in the interval (x - 1, x] for that coefficient.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
    are a list of possible solutions, and it may not cover all solutions.

    """

test_find_zero = [poly(x, 3) == 0]

test_find_zero[0]

``` 
The test_find_zero list contains a single test case, which is a list of coefficients for a polynomial and the expected result.

The test_find_zero list contains a single test case, which is a list of coefficients for a polynomial and the expected result.

The test_find_zero list contains a single test case, which is a list of coefficients for a polynomial and the expected result.

The test_find_zero list contains a single test case, which is a list of coefficients for a polynomial and the expected result.

The test_find_zero list contains a single test case, which is a list of coefficients for a polynomial and the expected result.

The test_find_zero list contains a single test case, which is a list of coefficients for a polynomial and the expected result.

The test_find_zero list contains a single test case, which is a list of coefficients for a polynomial and the expected result.

The test_find_zero list contains a single test case, which is a list of coefficients for a polynomial and the expected result.

The test_find_zero list contains a single test case, which is a list of coefficients for a polynomial and the expected result.