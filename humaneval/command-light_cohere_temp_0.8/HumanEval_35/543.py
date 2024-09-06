```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test the function with various input
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
assertEqual(max_element([1, 2, 3, 4, 5]), 5)
assertEqual(max_element([9, 2, 4, 3, 1, 8]) , 9)
```