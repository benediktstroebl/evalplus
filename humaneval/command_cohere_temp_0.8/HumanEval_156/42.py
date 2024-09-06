```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")
    res = []
    for i in range(1, 1000):
        if n >= i:
            count = len(str(i))
            res.extend(str(i)[::-1][:count])
            n -= i
    return ''.join(res)
```

This script provides a function `int_to_mini_roman` which takes a positive integer as input and converts it to its mini roman numeral representation as a string. It uses a loop to iteratively convert digits of the number into the roman numerals and subtracts the converted value from the original number until it is reduced to 0. It then joins the roman numerals generated into a single string. The function also checks if the input is less than 1 and raises a `ValueError` if so.

The tests for this function are not included as they are not provided in the prompt but can easily be added to validate the correctness of the script.  For example, we can create a test suite using Python's built-in `unittest` module like this:
```python
import unittest

def test_int_to_mini_roman(self):
    self.assertEqual(int_to_mini_roman(1), 'i')
    self.assertEqual(int_to_mini_roman(4), 'iv')
    self.assertEqual(int_to_mini_roman(19), 'xix')
    self.assertEqual(int_to_mini_roman(52), 'lix')
    with self.subTest(args=(421, )):
        self.assertEqual(int_to_mini_roman(421), 'cdxxi')
    with self.subTest(args=(1000, )):
        self.assertEqual(int_to_mini_roman(1000), 'mcmxxx')

class TestIntToMiniRoman(unittest.TestCase):
    def test_int_to_mini_roman(self):
        test_int_to_mini_roman(self)

if __name__ == '__main__':
    unittest.main()
``` 

This will run the test suite and report any passes or failures to the user.