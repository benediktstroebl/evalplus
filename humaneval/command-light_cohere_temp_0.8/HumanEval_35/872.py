```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test the function with various lists
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
print(max_element([1, 2, 3, 9, 4, 5, 6, 7, 8]))
print(max_element([19, 12, 5, 13, 6]))
print(max_element([-5, -10, -100]))
print(max_element([21, 22, -23]))
```
The function uses the built-in `max` function to return the maximum element in the list. In addition, the tests the list with different values to ensure that the function is well-defined and works correctly for all inputs.