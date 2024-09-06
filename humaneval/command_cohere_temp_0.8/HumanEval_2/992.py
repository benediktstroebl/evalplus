```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, as the leftover would be the decimal part of the number. 

To test this function, you can call it with a float value as follows: 
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
This will return 0.5 as the output, which is the decimal part of the number 3.5. 

The function should handle all positive floating point numbers, including integers (when `number` is an integer, the result will be 0.0). 

Let's add a simple test suite to cover both cases:
```python
import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_decimal(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_integer(self):
        self.assertEqual(truncate_number(5), 0.0)

if __name__ == '__main__':
    unittest.main()
``` 

When executing this file (via `python test_truncate_number.py`), the test suite will run, and assuming the function behaves as expected, there should be an output along the lines of: 
```
....
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
``` 
This indicates that the tests pass successfully.