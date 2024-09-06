```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test the function with some examples
assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) , [6, 4, 6, 3, 4, 4, 10, 1, 124])
```