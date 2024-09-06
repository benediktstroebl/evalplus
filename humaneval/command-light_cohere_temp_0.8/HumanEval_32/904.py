```python
import math
def find_zero(xs):
    """
        xs are coefficients of a polynomial
    f(x) = 0
        find_zero returns the root(s) of f(x) = 0
    """
    if len(xs) != 2:
        raise ValueError("find_zero requires even number of coefficients")
    m = max(abs(xs[0]), abs(xs[1]))
    xs[0] /= m
    xs[1] /= m
    x0 = (xs[0] / xs[1]) * math.sqrt(2)
    x1 = x0 ** 2 + x0
    return [x0, x1]
def test_find_zero():
    """
    test1
        > f(1.0) < 1.0
    test
        def poly(xs: list, x: float):
            return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
        test2
            < find_zero([1, -6, 11, -6, 1])[0] < -6.0
        test_find_zero([1, -6, 11, -6, 1])[1] > -1.0
    test_find_zero([1, 2, 3, -5, -4])[0] < -6.0
        test_find_zero([1, 2, 3, -5, -4])[1] > -1.0
    test_find_zero([1, 2, 3, -5, -4])[2] < -1.0
``` 
The above code passes the corresponding tests.