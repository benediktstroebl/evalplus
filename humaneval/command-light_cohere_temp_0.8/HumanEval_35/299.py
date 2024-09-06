```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst, default=float('-inf'))

# Test the function with some data.
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
The function `max_element` in this version directly uses the Python built-in `max()` function to discover the maximum element in the list. It also uses the's the default value for the `max` function, which is set to `float('-inf')` to guarantee that it handles empty and negative lists correctly. 
This function is then put through the test of the function by using it to calculate the maximum element of the given list.