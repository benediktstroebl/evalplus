```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
def test_positive_numbers():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.8) == 0.8
    assert truncate_number(12.01) == 0.01

test_positive_numbers()
```

The function `truncate_number` takes a float number as a parameter and returns the decimal part of the number. It does this by taking two integers and a fraction, `3.5` for instance would be `3 + 0.5`, the function takes the fraction and returns it, so `0.5` is the return for `3.5`. 

The test suite `test_positive_numbers` creates different scenarios for the function `truncate_number` and asserts that the return is correct. 

To run the test suite, import the `unittest` module and run the test suite:
```python
import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_positive_numbers(self):
        assert truncate_number(3.5) == 0.5
        assert truncate_number(7.8) == 0.8
        assert truncate_number(12.01) == 0.01

if __name__ == '__main__':
    unittest.main()
```
`unittest` will run the test suite and show the results, if the tests pass then it will show a message saying the tests were successful. 

If you do not have `unittest` installed you may do so with `pip`, running `pip install unittest` in your terminal. 

I hope this solution and added tests are suitable for what you may be looking for, let me know if you would like me to explain anything stated above!