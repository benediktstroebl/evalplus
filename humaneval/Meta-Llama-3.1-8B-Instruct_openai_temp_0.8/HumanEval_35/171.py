```python
def max_element(lst: list):
    """Return maximum element in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        int or float: The maximum element in the list.

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
This script defines a function `max_element` that takes a list of numbers as input and returns the maximum element in the list. The function uses the built-in `max` function to find the maximum element. If the list is empty, the function raises a `ValueError`. The script also includes example usage of the function.