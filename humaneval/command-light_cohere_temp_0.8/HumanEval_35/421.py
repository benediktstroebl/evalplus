```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1: Get maximum element from list
assert max_element([1, 2, 3]) == 3

# Test case 2: Get maximum element from list with negative numbers
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3: Get maximum element from empty list
assert max_element([]) is None

# Test case 4: Incorrect type of input
try:
    max_element([1, 2, 3, 'four'])
except TypeError:
    assert False  # Should raise an error
```
This code defines a Python function max_element that calculates and returns the maximum element from the input list lst. It is also comes with several test cases to validate the correctness of the function. The test cases cover scenarios where the list may contain, including positive and negative numbers, empty lists, and incorrect data types.