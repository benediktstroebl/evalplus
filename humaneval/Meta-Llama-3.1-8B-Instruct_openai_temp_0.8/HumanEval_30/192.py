```python
def get_positive(lst: list) -> list:
    """Return only positive numbers in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        list: A list of positive numbers.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in lst if num > 0]

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script uses a list comprehension to filter out the positive numbers from the input list. The `if num > 0` condition ensures that only numbers greater than 0 are included in the resulting list.