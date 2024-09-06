Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a short way of writing a for loop, to create a new list `x` that only includes elements `x` from the input list `l` that are greater than zero, thereby discarding all negative numbers. 

The function results can be easily asserted using Python's industry-standard `unittest` framework. Here is how you can do this:
```python
import unittest

class TestGetPositive(unittest.TestCase):
    def test_get_positive_basic(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_get_positive_more(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()
```
In the above code, `test_get_positive_basic` and `test_get_positive_more` are test cases that test the function get_positive with the given examples from the problem statement. 

The `unittest.main()` call runs the tests when the script is run directly. Here, `assertEqual` is a assertion function from the `unittest` framework that verifies that the two lists it is comparing are equal, and it will raise an exception if the assertion fails, alerting the user that the function does not behave as expected. 

Make sure to install the `unittest` framework with the command `pip install unittest` if you haven't already.  It is a part of the standard Python distribution and is widely used for testing Python scripts. 
If you run this script, the `unittest` framework will run the test suite and display the test results, including success messages or error messages in case of failure. 

This framework makes it easy to add more tests to this suite, enabling you to thoroughly test the `get_positive` function with a variety of input lists and assuring you that it will perform as expected.