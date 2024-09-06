```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x, returns f(x) = sum(xs)
    """
    return sum(xs)
def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero returns only zero point, even if there are many.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -1.0
    << "Not all coefficients are zero!"
```
This Python code defines two functions: `poly` and `find_zero`. The `poly` function calculates the sum of coefficients for a given list of coefficients (`xs`), and returns the result as a single value. The `find_zero` function attempts to find the zero point of a polynomial with coefficients given as input, and returns the result as a single value.

The code also includes test cases for both functions. The test cases demonstrate the test effectiveness by providing expected output and verifying that the function outputs match the expected values.