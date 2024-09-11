```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): A list of elements.

    Returns:
        int or float: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)


# Example usage:
numbers = [1, 2, 3]
max_num = max_element(numbers)
print(f"The maximum element in the list is {max_num}")

numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
max_num = max_element(numbers)
print(f"The maximum element in the list is {max_num}")
```

This script defines a function `max_element` that takes a list of elements as input and returns the maximum element in the list. It uses the built-in Python function `max()` to find the maximum element. The example usage demonstrates how to use this function with two different lists.