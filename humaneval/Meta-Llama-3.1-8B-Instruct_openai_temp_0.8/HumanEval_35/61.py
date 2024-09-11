```python
def max_element(lst: list) -> int:
    """
    Return maximum element in the list.

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

This Python script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. It uses the built-in `max` function to find the maximum element.

Note that the function is defined with type hints for the input list and the return value, and it includes a docstring that describes the function's behavior, including its arguments and return value, as well as some examples of its usage. The script also includes two test cases at the end to demonstrate the function's behavior.