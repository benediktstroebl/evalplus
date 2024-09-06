```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coefficient * math.pow(x, i) for i, coefficient in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x or one and only x.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    <<< round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -1.0
    <<< round(find_zero([3, 4, 3, 4]), 2) # 4x^2 + 4x = 3
    -2.0
    ```

def test_find_zero():
    """
    Test find_zero function
    Test find_zero function with coefficients [1, 2] against x = 1 and assert that the returned x = 1 is correct
    Test find_zero function with coefficients [-6, 11, -6, 1] against x = 1 and assert that the returned x = 1 is correct
    """
    assert find_zero([1, 2]) == 1
    assert find_zero([-6, 11, -6, 1]) == 1

def test_poly():
    """
    Test poly function
    Test poly function with coefficients [1, 2] against x = 1 and assert that the returned value is correct
    Test poly function with coefficients [-6, 11, -6, 1] against x = 1 and assert that the returned value is correct
    """
    assert poly([1, 2]) == 1 + 2*1 + 2*1**2 == 3.5
    <<< assert poly([-6, 11, -6, 1]) == -6 + 11*(-6) + (-6)*1**3 == -6 + 66 - 216 == -222
   

def test_find_zero():
    assert test_find_zero()

This script has a self-contained function `test_find_zero` that performs the following:

- It tests the `find_zero` function by passing various coefficient lists and checking that the returned `x` value matches the expected result.
- It also tests the `poly` function by passing coefficient lists and checking that the returned value matches the expected result.

This allows us to verify that the `poly` and `find_zero` functions are working correctly with different inputs.