```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of positive integers from the input list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Test cases
print(get_positive([-1, 2, -4, 5, 6]))  # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that uses a list comprehension to filter out non-positive numbers from the input list. It then includes example test cases to demonstrate the function's usage.