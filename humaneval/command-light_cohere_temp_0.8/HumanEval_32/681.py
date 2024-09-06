```python
import math
def find_zero(xs):
    """
    Find x-values where polynomial is zero.
    """
    xs = [float(i) for i in xs]
    if len(xs) % 2 != 0:
        raise ValueError("Input list must have even number of coefficients.")
    coeff = xs[0]
    for i in range(1, len(xs)):
        coeff += xs[i] * math.pow(i)
    x = coeff / (coeff**2 + x**2)
    return x
def test_find_zero(xs, x):
    """
    Test function to evaluate polynomial at point x
    """
    return find_zero(xs) == x
```