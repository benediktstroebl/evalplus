```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test the function with various lists
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123
print(max_element([1, 2, 3, -1000, 0, -100]))  # Output: -1000
print(max_element([-50, -20, -10, -1, 0, 50, 40, 30])) # Output: 50
print(max_element([1, 2, 3, 9, 8, 10, 7, 6]))  # Output: 9
```