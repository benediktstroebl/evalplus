### Maximum Element in a List
#### Python Script

```python
def max_element(lst: list) -> any:
    """Return maximum element in the list.

    Args:
        lst (list): A list of elements.

    Returns:
        any: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

# Example usage
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function called `max_element` that returns the maximum element in a given list. It uses Python's built-in `max` function to achieve this. If the list is empty, it raises a `ValueError` with a message indicating that the list is empty. The script includes example usage of the function to demonstrate its behavior.