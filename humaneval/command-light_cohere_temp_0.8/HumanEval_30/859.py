```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function with various lists
get_positive([-1, 2, -4, 5, 6])  # [2, 5, 6]
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # [5, 3, 2, 3, 9, 123]
get_positive([5, '3', -5, 2, -3, '31', 'abc', 12345])  # [5, 3, 123]
```