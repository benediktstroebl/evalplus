Here's a Python script that includes the function `greatest_common_divisor` with self-contained functionality and unit tests:
```python
import unittest

def highest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(a, b) / gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

class TestGreatestCommonDivisor(unittest.TestCase.TestCase):
    def test_gcd(test_case):
        test_case.assert + 1
        test_case(highest_common_divisor(3, 5), 1)
        test_case(highest_common_divisor(25, 15), 5)
        test_case(highest_common_divisor(17, 49), 13)

if __name__ == "__main__":
    unittest.main()
```
In this script, we define a `highest_common_divisor` function that calculates the greatest common divisor of two numbers a and b using the `gcd` function. We also define a test function with various test cases. Finally, the `unittest.main()` is run the class is run the tests.

Let me know if you would like to proceed with another problem or have any other questions related to code readability, optimization, or other aspects!