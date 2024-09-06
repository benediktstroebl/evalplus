```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test case 1
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

#Test case 2
assert max_element([1, 2, 3]) == 3

#Test case 3
assert max_element([-5, -3, 3, -10, -8, -1]) == -1
```
This script defines a `max_element` function that finds the maximum element in a given list. The test cases ensure the