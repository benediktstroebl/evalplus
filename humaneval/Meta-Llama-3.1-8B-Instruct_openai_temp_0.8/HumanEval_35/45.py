```python
def max_element(lst: list) -> int:
    """
    This function returns the maximum element in a given list.

    Args:
        lst (list): A list of elements.

    Returns:
        int: The maximum element in the list.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("List is empty")

    return max(lst)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, we define a function `max_element` that takes a list `lst` as input and returns the maximum element in the list. We use the built-in `max` function in Python to find the maximum element. If the list is empty, we raise a `ValueError` because there is no maximum element in an empty list. The example usage at the end demonstrates how to call this function with different lists.