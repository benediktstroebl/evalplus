```python
def get_positive(numbers: list) -> list:
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of positive numbers from the input list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Test cases
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```

This Python script defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. It uses list comprehension to create the new list. The script includes docstrings and example usage to demonstrate the function's behavior.