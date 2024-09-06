```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle.
    Return True if the three sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is a right angle or 
    90 degree.
    """
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False
```
The following tests would be useful to ensure the function works correctly:
```python
import unittest
class TestRightAngleTriangle(unittest.TestCase):
    def test_valid_1(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))

    def test_valid_2(self):
        self.assertTrue(right_angle_triangle(5, 12, 13))

    def test_invalid_1(self):
        self.assertFalse(right_angle_triangle(1, 2, 3))

    def test_invalid_2(self):
        self.assertFalse(right_angle_triangle(3, 7, 4))
    def test_invalid_3(self):
        self.assertFalse(right_angle_triangle(2, 2, 1))
    def test_invalid_4(self):
        self.assertFalse(right_angle_triangle(10, 2, 5))
if __name__ == '__main__':
    unittest.main()
```
We use unittest in Python to test the functionality of the function `right_angle_triangle`. The `TestRightAngleTriangle` class derives from `unittest.TestCase` and contains several test methods. Each test method is named starting with `test_` and performs a specific test. For example, `test_valid_1` tests whether the function returns True for a valid input (3, 4, 5), and `test_invalid_1` tests whether the function returns False for an invalid input (1, 2, 3). You can add more test methods according to different test scenarios. Running the module executes all the test methods. The `assertTrue` method is used when the test expects a True outcome, and `assertFalse` is used when the test expects a False outcome.  If all tests pass with no exceptions, you will see output that indicates that all tests have passed. It will look like this:
```bash
....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
``` 

If you intend to get the result, please ensure that the Python script is saved in a Python file with a .py extension (e.g., right_angle_triangle.py) and execute the file in your Python interpreter.

This approach provides a robust testing mechanism to validate the correctness of the function and ensures that it behaves as expected for different inputs.