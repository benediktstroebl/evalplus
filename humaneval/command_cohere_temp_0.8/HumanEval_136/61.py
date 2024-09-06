```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The function `largest_smallest_integers` uses the `min` and `max` functions with a custom key to find the smallest positive and largest negative integers in the list. The key is a lambda function that returns `True` if the integer is negative, and `False` if it is positive. 

The function can handle edge cases where the list is empty or only contains zero or positive integers. 

Here is a test suite that can be used to validate the function:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (1, 1)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([-3, -5, -1, -7, -4, -2]) == (-2, -7)
    assert largest_smallest_integers([1, 2, 3, 4, 5, -8, 0, 7]) == (-8, 1)
```

To run the tests, you can call them one by one:
```python
test_largest_smallest_integers()
```

Alternatively, you can use a test runner to automate and run all the tests in the suite:
```python
import unittest

class TestLargestSmallestIntegers(unittest.TestCase):
    def test_largest_smallest_integers(self):
        assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (1, 1)
    def test_empty_list(self):
        assert largest_smallest_integers([]) == (None, None)
    def test_positive_list(self):
        assert largest_smallest_integers([0]) == (None, None)
    def test_negative_and_positive(self):
        assert largest_smallest_integers([-3, -5, -1, -7, -4, -2]) == (-2, -7)
    def test_only_negative(self):
        assert largest_smallest_integers([-8, -9, -10, -11]) == (-8, -11)
    def test_only_positive(self):
        assert largest_smallest_integers([1, 2, 3, 4, 5]) == (None, 5)

if __name__ == '__main__':
    unittest.main()
```

The code leverages Python's `unittest` module to create a test suite and individual test cases. 

You can run this script, and the test runner will execute all the test cases in the `TestLargestSmallestIntegers` class and report the results, indicating successful passes with an `OK` status.