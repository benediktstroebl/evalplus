```python
def get_positive(numbers: list) -> list:
    """
    Return only positive numbers in the list.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A list of positive integers.

    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]
```

You can run this script and use it as a function to filter out positive numbers from any list of integers.