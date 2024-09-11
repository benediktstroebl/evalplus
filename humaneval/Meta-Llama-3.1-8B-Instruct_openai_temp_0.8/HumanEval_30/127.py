```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
    numbers (list): A list of numbers.

    Returns:
    list: A list of positive numbers from the input.

    Example:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Test the function
numbers = [-1, 2, -4, 5, 6]
result = get_positive(numbers)
print(result)  # Output: [2, 5, 6]

numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(numbers)
print(result)  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script uses a list comprehension to filter the input list and return a new list containing only the positive numbers.