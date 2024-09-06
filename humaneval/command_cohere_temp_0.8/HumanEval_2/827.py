```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter into an integer and then returns the difference between the original number and the integer. The result is the decimal part of the original number.

To test this function, you can call it with a few test cases like so:
```python
# Testing Truncate Number Function
import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertEqual(truncate_number(3.5), 0.5)
        self.assertEqual(truncate_number(2.0), 0.0)
        self.assertEqual(truncate_number(1.1), 0.1)
        self.assertEqual(truncate_number(0.5), 0.0)

if __name__ == '__main__':
    unittest.main()
```
This will run the test suite and verify that the function `truncate_number` behaves as expected.