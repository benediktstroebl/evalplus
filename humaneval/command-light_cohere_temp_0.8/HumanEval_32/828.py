```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    # Test by checking if poly(x) == 0 using the above function
    # Test 1: all coefficients are even numbers greater than 1
    assert find_zero([2, 4, 6, 8]) == (2 * math.pow(2) + 4 * math.pow(3) + 6 * math.pow(4) + 8 * math.pow(5))
    Test 2: all coefficients are equal to 1
    assert find_zero([1, 1, 1, 1]) == (1 * math.pow(1) + 1 * math.pow(2) + 1 * math.pow(3) + 1 * math.pow(4))
   
    Test 3: coefficients are -6, 11, -6, 1
    assert find_zero([-6, 11, -6, 1]) == (-6 * math.pow(1) + 11 * math.pow(2) + -
Test 4: coefficients are 1, 2, 3, 4
    assert find_zero([1, 2, 3, 4]) == (1 * math.pow(1) + 2 * math.pow(2) + 3 * math.pow(3) + 4 * math.pow(4))
```
The script defines two functions: poly and find_zero. The poly function calculates the polynomial with coefficients xs and x. The find_zero function finds the zero of the polynomial.