```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with various inputs
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123])
assertEqual(get_positive([]), [])
assertEqual(get_positive([-123]), [])
assertEqual(get_positive([234, -5, -23, 4]), [234, -23, 4])

```

This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the input list. The function is then tested with various inputs to ensure it works correctly.