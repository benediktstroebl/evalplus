```python
import math

def find_zero(xs):
    """
    Validate input
    assert len(xs) % 2 == 0, "Input must have an even number of coefficients."
    assert xs[-1] != 0, "Last coefficient cannot be zero"

    coeffs = [x for x in xs if x != 0]
    return coeffs

def poly(xs, x):
    """
    Evaluate polynomial with coefficients xs at point x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero():
    """
    Test function
    """
    assert find_zero([1, 2]) == (1 + 2*x) - 0.5, "Invalid output"
    assert find_zero([-6, 11, -6, 1]) == (-6 + 11*x) - 0.5, "Invalid output"
```