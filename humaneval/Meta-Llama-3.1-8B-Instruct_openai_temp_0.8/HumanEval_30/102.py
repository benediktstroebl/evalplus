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

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script uses a list comprehension to filter out non-positive numbers from the input list. The expression `num > 0` is used as a condition to include numbers in the output list. The function takes a list of integers as input and returns a new list containing only the positive integers from the input list.