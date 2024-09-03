```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.
    """
   
   
    sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial (xs)(x) = 0
    find_zero returns only zero point, even if there are many
    solutions.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
    # Verify that the polynomial is correct
    e.x + 5 *x
    - should equal 1 + 3x - 2.0
    -1.5
    -2,
    >>> round(poly([1, 2, 3]), 2) # f(x) = 1 + 3x - 2
    -0.0.
    >>> round(poly([1, 2, 3]), 2) # f(x) = 1 + 3x - 2
    -0.0.
    ```
```