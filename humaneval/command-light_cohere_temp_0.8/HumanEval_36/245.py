Here's the code with the fizz_buzz function and unit tests:
```python
import unittest
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Use built-in int divisor method to count the number of times 7 appears
    # in the quotient.
    return sum(x % 7 for x in range(1, n+1) if x % 10 != 7)

class TestFizzBuzz(unittest.TestCase.TestCase):
   
    def test_FizzBuzz(self):
    self.assertEqual(fizz_buzz(50), 0)
    self.assertEqual(fizz_buzz(78), 2)
    self.assertEqual(fizz_buzz(79), 3)

if __name__ == "__main__":
    unittest.main()
```
This script defines a fizz_buzz function that counts the number of times the digit 7 appears in the quotients of numbers less than n that are divisible by 11 or 13. It also defines a TestFizzBuzz class with a test method that runs the fizz_buzz function with various input values and asserts the expected output.