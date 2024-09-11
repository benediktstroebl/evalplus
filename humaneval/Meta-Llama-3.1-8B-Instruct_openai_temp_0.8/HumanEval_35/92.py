```python
def max_element(lst: list):
    """
    Return the maximum element in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        The maximum element in the list.

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

In this script, we define a function `max_element` that takes a list of numbers as input and returns the maximum element using the built-in `max` function. We then test the function with the provided examples in the `if __name__ == "__main__":` block.