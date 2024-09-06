```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the max_element function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
# Use the function with custom list
result = max_element([1, 2, 3, -20, -100, 5, 6, 7])
assert result == 5
```