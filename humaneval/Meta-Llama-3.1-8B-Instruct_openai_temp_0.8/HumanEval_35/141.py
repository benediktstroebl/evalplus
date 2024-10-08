```python
# max_element.py

def max_element(lst: list) -> int:
    """
    Return the maximum element in the list.

    Args:
    lst (list): A list of integers.

    Returns:
    int: The maximum element in the list.

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(lst)


# Test the function
if __name__ == "__main__":
    print(max_element([1, 2, 3]))  # Expected output: 3
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. The function uses Python's built-in `max` function to find the maximum element. The docstring provides documentation for the function, including a description, input parameters, return value, and examples of usage. The script also includes a test section at the bottom to verify the function's correctness.