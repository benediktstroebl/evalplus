```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with various inputs
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123])
assertEqual(get_positive([9, 7, 5, -2]), [9, 7])
assertEqual(get_positive([19, 2, 14, 9, 1]), [19, 2, 14, 9])

```