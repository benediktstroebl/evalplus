```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): A list of elements.

    Returns:
        The maximum element in the list.

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
if __name__ == "__main__":
    print(max_element([1, 2, 3]))  # Output: 3
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list as input and returns the maximum element. It uses the built-in `max` function to achieve this. If the list is empty, it raises a `ValueError` to handle invalid input. The example usage at the end demonstrates how to use the `max_element` function with sample lists.