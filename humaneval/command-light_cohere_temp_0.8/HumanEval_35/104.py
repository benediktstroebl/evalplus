```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test case 1:
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

#Test case 2:
assert max_element([]) == 0

#Test case 3:
assert max_element([10, 9, 3, -15]) == 9
```