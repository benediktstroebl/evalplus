```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test case 1:
assert max_element([1, 2, 3]) == 3

# Test case 2:
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```
The function max_element takes a list as input and uses the built-in max() function to return the maximum element in the list.

The function is then tested with two different lists, and the results are compared with the expected maximum element values.