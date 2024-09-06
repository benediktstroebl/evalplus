```python
def max_element(l: list):
    """Return maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```

The `max_element` function takes a list `l` as an argument and uses the `max` function to return the maximum value in the list. 

The "unittest" module is used to test the function with different inputs:
```python
import unittest

class TestMaxElement(unittest.TestCase):
    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_max_element_with_negative_values(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main()
```

The `unittest` framework is used to organize and run tests. The `TestMaxElement` class inherits from `unittest.TestCase` and defines test methods starting with the word `test`. The `assertEqual` method is used to check if the actual result of the function is equal to the expected value.