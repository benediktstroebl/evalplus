```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst, default=float('-inf'))

# Test cases
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([-5000, -3000, -1000, 0, 1000, 7000, 8000]))  # Output: 7000
print(max_element([1, 2, 3, 100, 200, 300, 400, 500]))  # Output: 500
print(max_element([77, 90, 73, 58, 11, 0]))  # Output: 77
```