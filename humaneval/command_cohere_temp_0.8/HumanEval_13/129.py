```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The `greatest_common_divisor` function employs recursion to find the greatest common divisor (GCD) of two integers `a` and `b`. It leverages the property that the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y`. If `b` is 0, it returns `a` (as `b` cannot evenly divide `a` in this case). Otherwise, it recursively calls itself with the arguments swapped, applying the fundamental arithmetic equation `GCD(b, a % b) = GCD(a, b)`. This approach efficiently calculates the GCD of the input values. 

Here is a test suite for this function:
```python
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 180) == 180
    assert greatest_common_divisor(36, 60) == 12
    assert greatest_common_divisor(-7, -35) == 1
    assert greatest_common_divisor(16, 8) == 8
    assert greatest_common_divisor(0, 0) == 0
```

To execute the tests, you can run the script from the Python environment console using the command `python script_name.py`. The `test_greatest_common_divisor()` function will execute the `greatest_common_divisor` function with different arguments and verify if the results match the expected values.  This will help ensure the correct functionality of the `greatest_common_divisor` function.  If all tests pass, you will see output indicating that all assertions passed. If any test fails, you will see an error message specifying which assertion failed.  This provides an assurance that the function works as expected.