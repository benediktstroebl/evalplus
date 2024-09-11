```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): A list of elements.

    Returns:
        int or float: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    # Check if the list is not empty
    if not l:
        raise ValueError("List is empty")

    # Use built-in max function to find the maximum element
    return max(l)


# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list of elements as input and returns the maximum element in the list. It uses the built-in `max` function to find the maximum element, which has a time complexity of O(n), where n is the number of elements in the list.

The script also includes docstrings to provide documentation for the function and test the function with some examples. If the input list is empty, the function raises a ValueError with a message indicating that the list is empty.