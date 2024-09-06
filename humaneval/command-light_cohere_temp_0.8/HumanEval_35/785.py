```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3
assert max_element([]) == 0

# Test case 4
try:
    x = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    x.sort()
    sort(x)
    assert max_element(x) == 123
```