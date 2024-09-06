```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. 

To test this function, here is a set of sample tests: 

```python
# Test suite
import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number_with_positive_float(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_truncate_number_with_scientific_notation(self):
        self.assertEqual(truncate_number(3.5142), 0.1402)

    def test_truncate_number_with_negative_float(self):
        self.assertEqual(truncate_number(-3.5), -0.5)

    def test_truncate_number_with_zero(self):
        self.assertEqual(truncate_number(0.0), 0.0)

    def test_truncate_number_with_one(self):
        self.assertEqual(truncate_number(1.0), 0.0)

if __name__ == '__main__':
    unittest.main()
``` 

If you want to check the documentation, the function accepts a number and returns the decimal part of the number.