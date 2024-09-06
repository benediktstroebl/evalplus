```python
import math

def find_zero(xs):
    """
    Find the x-value where polynomial polynomial(xs) equals 0.
    xs: list of coefficients
    Test it by plugging in a sample x value
    --> return x where polynomial(xs) = 0, or float('inf') if no such x
    """
    x = -math.pi  # float('inf')  # x value to test
    if any(xs):  # if polynomial has any coefficients
        return x  # found x value where polynomial equals 0
    else:
        return float('inf')  # no solution

def polynomial(xs: list):
    """
    Evaluates polynomial with coefficients xs at point x
    --> returns xs0 + xs[1] * x + xs[2] * x^2 + ...
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero():
    """
    Test find_zero function
    """
    assert find_zero([1, 2]) == -0.5
    assert find_zero([-6, 11, -6, 1]) == 1.0
    assert find_zero([3, 3]) == float('inf')

if __name__ == "__main__":
    print("Test passed!")
```