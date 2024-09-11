```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
    numbers (list): A list of numbers.

    Returns:
    list: A list of positive numbers from the input list.

    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # Use list comprehension to filter out non-positive numbers
    return [num for num in numbers if num > 0]
```

This script defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. The function uses list comprehension to achieve this, which is a concise way to create a new list by applying a condition to each element in the input list. The condition `num > 0` checks if a number is positive, and if it is, the number is included in the new list.