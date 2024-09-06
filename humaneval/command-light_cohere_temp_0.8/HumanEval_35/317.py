```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test cases
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]) == 123
```

This script defines a function `max_element` that finds and returns the maximum element in the passed list. The test cases ensure the right behavior for the function.