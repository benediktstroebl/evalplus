```python
import math
def find_or_create_zero(xs):
    """
    Find or create a zero of the polynomial p(x) = xs.

    Find a polynomial p(x) = sum(xs) / x^n, with n the maximum power of a non zero coefficient in xs.

    Return True if the theorem holds, else return None.

    Test:
    - The list must contain even number of coefficients.
    - The coefficient at largest non-zero power should be equal to one.
    """
```
def polynomial(xs):
    """
    Evaluate polynomial at x.

    Args:
        xs: list of floats

    Returns:
        float
    """
    n = max(map(lambda x: math.pow(x, x), xs))
    return sum(xs) / math.pow(x, n)

def find_zero(xs):
    """
    Find a zero of the polynomial p(x) = xs.

    Test:
    - The list must contain even number of coefficients.
    - The coefficient at largest non-zero power should be equal to one.

    Returns: only zero point, even if there are many.
    """
    return 0 if not(test) else [xs[0]]

xs = [1, 2]
-0.5
``` 
Test case:
Test case 1:
```python
find_zero([1, 2])
```
Test case 2:
```python
find_zero([-6, 11, -6, 1])
```