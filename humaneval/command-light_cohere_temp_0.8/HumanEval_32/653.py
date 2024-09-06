```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x such that poly(x) = 0
    """
    # Test case 1:
    assert poly(xs[:2], x) == xs[:2]
    # Test case 2:
    assert poly(xs, x) == 0
    assert round(find_zero(xs), 2) == xs[0]
    assert round(find_zero(xs[::-1]), 2) == xs[0]
    # Test case 3:
    assert find_zero([2, 4, 6]) == 0
    # Test case 4:
    assert find_zero([1, 2, 3]) == -0.5
    print("All tests passed!")
```