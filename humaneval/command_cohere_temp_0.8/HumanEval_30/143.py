Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a short way of writing a for loop, to create a new list `x` that includes only the positive elements of the input list `l`. The expression `x for x in l if x > 0` creates a new list with elements `x` from the list `l` that are greater than zero. The result is the list of positive numbers in the input list. 

Here's how you can test it with Python's built-in `unittest` module:
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
This script uses Python's `unittest` module to create two test cases: `test_get_positive_basic` and `test_get_positive_more`. The `assertEqual` method checks if the output of `get_positive` gives the expected result. When you run this script, the `unittest` module runs these tests and tells you whether the tests pass or fail.  By doing this, you can ensure that your function behaves as expected, which is especially valuable in software development to guarantee the reliability of your code.