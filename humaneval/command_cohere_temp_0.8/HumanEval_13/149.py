```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive algorithm is inspired by the Euclidean algorithm. It exploits the property that the greatest common divisor of two integers `a` and `b` is equal to the greatest common divisor of `b` and `a % b`. When `b` is 0, the algorithm returns `a`, which is the gcd of `a` and 0.

To verify the correctness of the algorithm, let's run tests using Python's built-in `unittest` module:
```python
import unittest

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_gcd_1(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_gcd_2(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_gcd_3(self):
        self.assertEqual(greatest_common_divisor(0, 75), 0)

    def test_gcd_4(self):
        self.assertEqual(greatest_common_divisor(75, 0), 0)

if __name__ == '__main__':
    unittest.main()
```
Let's break down the testing code:
1. `import unittest`: This imports Python's built-in module for testing.
2. `class TestGreatestCommonDivisor(unittest.TestCase)`: This creates a test class which derives from `unittest.TestCase`. This class provides a number of methods that serve as useful shortcuts for writing test operations and asserting equality.
3. `def test_gcd_1(self)`: `test_gcd_1` is a test function inside the test class. `self` is a first parameter required by every method of a class derived from `unittest.TestCase`, and it refers to the current instance of the class, which in this case is our test class.
4. `self.assertEqual(greatest_common_divisor(3, 5), 1)`: The `assertEqual` method tests if the first argument is equal to the second argument and fails the test if the two values are not equal.
5. The method `if __name__ == '__main__':` checks if the script is being run directly by Python or being imported as a module.
6. `unittest.main()` refers to the `main` function of the `unittest` module which runs all the tests inside the class. 

To run the tests, you can run this Python script directly in your terminal. You can also import this script into an existing Python project and run tests using a test runner tool like `pytest`.