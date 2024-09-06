```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t` using the `<` operator. The `all()` function returns `True` if all comparisons are `True`, indicating that all elements are below the threshold, otherwise `False`. 

Here is a simpler alternative solution using a list comprehension:
```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This alternative solution leverages a list comprehension, offering a more concise approach to assess whether all list elements are below the threshold.

Both solutions assume that the input list `l` is non-empty and that the threshold `t` is a single value.

The function above_threshold can be tested very easily using the Python `unittest` module like this:
```python
import unittest

class TestBelowThreshold(unittest.TestCase):
    def test_below_threshold_all_less(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_below_threshold_all_greater(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

    def test_below_threshold_empty_list(self):
        self.assertFalse(below_threshold([], 100))

if __name__ == '__main__':
    unittest.main()
```
In the test method `test_below_threshold_empty_list` we check if the function returns `False` when the input list is empty, this is a boundary case that needs to be considered because the `all()` function returns `False` when no items are evaluated.  The `unittest` module provides a simple and standardized way to organize and run tests, and `assertTrue` and `assertFalse` are used to verify that the function returns the expected result based on specific inputs and expected conditions.  The `if __name__ == '__main__':` line ensures that the test suite runs when the script is executed directly.  It is important to have test coverage for different scenarios in order to maintain the reliability of the function.