```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return math.sqrt(max(a, b))

# unit tests
test_gcd = GreatestCommonDivisorTestCase()
test_gcd.test_gcd()
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b using the `math.sqrt()` function, which requires that both inputs are numbers. The code also includes a unit test suite called `test_gcd` which contains a single test method that checks if the `greatest_common_divisor` function passes all the tests correctly.