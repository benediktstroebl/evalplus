```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm works by the Euclidean algorithm concept, which states that the gcd of two numbers `a` and `b` is the same as the gcd of `b%a` and `a`. In the case where `a` is 0, it returns `b` because `b%a` defaults to `b` and it avoids an infinite loop. 

Here is a test suite for this function:
```python
def test_gcd():
    """
    Tests the greatest_common_divisor function.
    """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 25) == 25
    assert greatest_common_divisor(10, 0) == 0
    assert greatest_common_divisor(0, 0) == 0
```
This test suite includes tests for edge cases like zero arguments, as well as a regular case. 
To run the tests, you can save the test suite into a Python file (e.g., `test_gcd.py`) and then run the file using the Python interpreter:
```bash
python test_gcd.py
```
The `assert` statements will ensure that each test case passes, giving you confidence in the correctness of the `greatest_common_divisor` function.  If any of the tests fail, `AssertionError` will be raised, and the test suite will report the failures, helping you identify areas that need improvement.  This approach makes it easy to validate changes to the function in the future.  If you prefer a more automated approach, you can use a continuous integration (CI) tool like Travis CI or GitHub Actions to run your test suite on every commit or merge request, enforcing test coverage and preventing regressions.  This is especially useful for larger projects or teams where manual testing can be time-consuming.