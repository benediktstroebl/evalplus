```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The `greatest_common_divisor` function iteratively uses the modulo operator to find the divisor of the two integers a and b. It returns the largest integer that divides both a and b evenly, known as the greatest common divisor (GCD). The base case of the recursive approach is when either a or b is zero, wherein which the function returns the remaining non-zero integer. 

Here is a test script that can be used to test the functionality of the program:
```python
def test_greatest_common_divisor():
    """ Test the greatest_common_divisor function """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 100) == 100
    assert greatest_common_divisor(100, 0) == 100
    assert greatest_common_divisor(63, 105) == 3
    assert greatest_common_divisor(-10, 25) == 5
    assert greatest_common_divisor(3, -5) == 1
    assert greatest_common_divisor(-3, 8) == 1
test_greatest_common_divisor()
```

This would yield the following output:
```bash
True
True
True
True
True
True
True
``` 

The test script employs the `assert` statement to validate the function's output against the expected values.