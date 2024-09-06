```python
import math
def find_zero(xs):
    """
    Find x-values that satisfy polynomial equation.
    """
    xs are coefficients of a polynomial. Check even number of coefficients.
    return [ only zero solution if even list has even number of coefficients and the largest coefficient is non-zero.
    return list([x, 0]) if even, else return []
  return
# Example usage
xs = [1, 2,3,1,-6,11,-6,1]
result = find_zero(xs)
assert len(result) == 4
assert result[0] == 0
assert result[1] == 0
assert result[2] == 1
assert result[3] == 0
assert result[4] == 1
```