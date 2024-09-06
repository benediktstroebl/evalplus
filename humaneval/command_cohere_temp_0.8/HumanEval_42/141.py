Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with its elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

Here's a markdown code block with the above Python code:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function can be tested with the following Python code:
```python
# Test incr_list function
import unittest

class TestIncList(unittest.TestCase):
    def test_incr_list(self):
        # Regular usage of incr_list function
        assert incr_list([1, 2, 3]) == [2, 3, 4]
        assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

    def test_incr_list_with_negative_values(self):
        # Handling negative values in the input list
        assert incr_list([-5, -3, -11, -1, -7]) == [{-4, -2, -12, -2, -8}]

    def test_incr_list_with_float_values(self):
        # Handling float values in the input list
        assert incr_list([1.5, 2.0, 3.5, 4.0, 3.0, 1.0]) == [2.5, 3.0, 4.5, 5.0, 4.0, 2.0]

    def test_incr_list_with_non_numeric_values(self):
        # Handling non-numeric values in the input list
        assert incr_list([1, 2, '3', 4, '5', 6]) == [2, 3, '4', 5, '6', 7]
        # Test the incr_list function with a mixed input list
        mixed_list = [1, 2, '3', 4, '5', 6, 7.8, -3, 10, 'foo']
        assert incr_list(mixed_list) == [2, 3, '4', 5, '6', 7, 7.8, -2, 11, 'foo']

if __name__ == '__main__':
    unittest.main()
```

This test code uses the `unittest` module to ensure that the `incr_list` function works correctly with various input types.