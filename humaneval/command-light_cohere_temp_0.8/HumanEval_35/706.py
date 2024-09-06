```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test case 1: Basic list with positive and negative numbers
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 2: List with additional element: 0
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, 0]) == 123

# Test case 3: List with additional element: NaN
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, float('nan'))) == float('nan')

# Test case 4: List with additional element: Infinity
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, float('inf')]) == float('inf')

# Test case 5: Empty list
assert max_element() is None
```