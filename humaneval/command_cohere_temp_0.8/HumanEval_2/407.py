```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which is the basic definition of the decimal part of a number. 

To test this function, you can call it with a few different floating point numbers and compare the result to the expected output. 

For example, given the input `3.5`, the function should return `0.5`, since the integer part of 3.5 is `3` and the decimal part is `0.5`. 

To see the function in action, you can run the following code:
```python
truncate_number(3.5) == 0.5
# True

truncate_number(2.0) == 0.0
# True

truncate_number(1.5) == 0.5
# True
``` 
or even better, use unittest to test your function:
```python
import unittest

def truncate_number(number):
    return number - int(number)

class TestTruncateNumber(unittest.TestCase):
    def test_positive_float(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_positive_decimal(self):
        self.assertEqual(truncate_number(2.0), 0.0)

    def test_positive_fraction(self):
        self.assertEqual(truncate_number(1.5), 0.5)

if __name__ == '__main__':
    unittest.main()
``` 
This should produce the following output:
```bash
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
``` 
Make sure to have the unittest module installed, if so, the command above will execute the test suite and inform of the result.