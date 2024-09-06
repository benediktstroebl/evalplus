```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x,
    returns sum of xs coefficients multiplied by corresponding powers of x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Find x value that makes polynomial equal to zero
    """
    return min(xs, key=lambda x: poly(xs) == x)
# Test cases
xs = [1, 2, -5]
x = float('inf')
ans = find_zero(xs)
assert x == ans, "Value not found!"
xs = [1, 0, -1]
x = 0
ans = find_zero(xs)
assert x == ans, "Value not found!"
xs = [0, 1, -1]
x = 2
ans = find_zero(xs)
assert x == ans, "Value not found!"
xs = [1, -1, -1]
x = float('inf')
try:
    ans = find_zero(xs)
    assert x == ans, "Value not found!"
except:
    assert False, "Should have found the root"

print("All tests passed!")
``` 
This script defines a function 'poly' which evaluates a polynomial with coefficients provided as a list at a given point, and 'find_zero' which finds the root of a polynomial given as an input list of coefficients.

The 'test cases' section provides a set of test cases to pass. If all test cases pass without any assertion error, the script prints "All tests passed!".