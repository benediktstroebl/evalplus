```python
def max_element(l: list) -> int:
    """Return maximum element in the list."""
    if not l:
        raise ValueError("List is empty")
    return max(l)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list `l` as input and returns its maximum element. It uses Python's built-in `max` function to find the maximum element, which has a time complexity of O(n), where n is the number of elements in the list. If the list is empty, it raises a `ValueError`. The example usage at the end demonstrates how to use the function with some example lists.