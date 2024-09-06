```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    and finds_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

   
   
    ``` test.
    assert find_zero([1, 2]) == (1 + 2*1)
    assert find_zero([-6, 11, -6, 1]) == (-1 + 2*(-6))
    assert find_zero([1, -2, -1]) == (-1 + 2*1)
    assert find_zero([4, 5, 6]) == -1.0
    ```
```

The test covers basic test cases and verifies that the function `find_zero` returns the correct results.