Here's a Python script that implements the `max_element` function and includes some example usage:
```python
def max_element(lst: list) -> int:
    """Return maximum element in the list."""
    if not lst:
        raise ValueError("List cannot be empty")
    return max(lst)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123

# Test case with empty list:
try:
    print(max_element([]))
except ValueError as e:
    print(e)  # Output: List cannot be empty
```
In this implementation, the `max_element` function uses Python's built-in `max` function to find the maximum element in the list. If the list is empty, it raises a `ValueError`.