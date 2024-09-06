```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    return max(a, b) // gcd(a, b)

# Test case function
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
```
The test case function `test_greatest_common_divisor()` asserts that the `greatest_common_divisor()` function correctly returns the greatest common divisor of the given inputs.

This code, which has a self-contained function and test case, can be used to solve the problem of finding the greatest common divisor between two integers.