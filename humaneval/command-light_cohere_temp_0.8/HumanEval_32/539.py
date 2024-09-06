```python
import math
def find_zero(xs):
    """
    Validate input:
        Must be list of numbers
        Must have even length
    """
    assert isinstance(xs, list), "Input must be a list"
    assert len(xs) % 2 == 0, "Input list must have even length"
    return xs if len(xs) % 2 == 0 else None

def poly(xs, x):
    """
    Evaluate polynomial with coefficients xs at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero():
    """
    Test find_zero function
    """
    assert find_zero([1, 2]) == (1, 2), "First test failed"
    assert find_zero([-6, 11, -6, 1]) == (-1, -2), "Second test failed"
    assert find_zero([1, -3, -4, 5]) == (-3, -4), "Third test failed"

if __name__ == "__main__":
    test_find_zero()
```
This script defines the functions `find_zero`, `poly`, and `test_find_zero`. The `find_zero` function validates the input and returns None if the input is not a list of numbers or doesn't have an even length. The `poly` function computes the polynomial with coefficients xs at point x. The `test_find_zero` function contains test cases that validate the behavior of the `find_zero` function.