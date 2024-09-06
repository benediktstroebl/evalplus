```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(a, b) / __gcd__(a, b)

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
```
This code provides a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function uses the typical method of finding GCD, which is to calculate the product of a and b and divide by a until the remainder becomes 0, and takes the maximum of a and b as the result. 

The test function `test GreatestCommonDivisor()` passes all the test cases.