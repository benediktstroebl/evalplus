```python
import math

def find_zero(xs):
    """
   xs are coefficients of a polynomial
    find_zero finds x such that polynomial xs(x) = 0
    find_zero returns None if there are no solutions, otherwise, it returns the smallest possible solution.
    """
    test:
    assert find_zero([1, 2]) == -0.5
    assert find_zero([-6, 11, -6, 1]) == 1.0
    ```

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
```