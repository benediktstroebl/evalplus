```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Basic test case
test_max_element = [1, 2, 3]
assert max_element(test_max_element) == 3

# List with negative elements
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_list) == -3

# List with positive and negative numbers
test_mixed = [1, 2, 3, 5, -10, 123]
assert max_element(test_mixed) == 5
``` 
This Python script defines a function max_element that calculates and returns the maximum element in a given list. It is then be used as part of larger codebases and is fully self-contained within the Python interpreter.