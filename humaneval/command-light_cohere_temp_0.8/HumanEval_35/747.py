```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test the function with various lists
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([-5, -20, 0, 7, 3, -100]))  # Output: 0
print(max_element([-55, -65, -90, 90, 75, 60, 25]))  # Output: 75
print(max_element([1, 2, 3, 4, 5, 6, 7]))  # Output: 5
```