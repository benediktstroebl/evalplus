```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert max_element([]) == 0
assert max_element([10, 10, 10]) == 10
assert max_element([5, 10, 10, 10, 50]) == 10
```
This script defines a function `max_element` that returns the maximum element in a list. The test cases cover various scenarios, passing the test with different lists and edge cases.