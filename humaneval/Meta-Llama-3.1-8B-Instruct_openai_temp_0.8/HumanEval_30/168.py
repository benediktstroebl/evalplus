```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
    numbers (list): A list of numbers

    Returns:
    list: A list containing only the positive numbers from the input list

    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]
```

This script uses list comprehension, a feature of Python that allows you to create a new list by performing an operation on each item in an existing list. The code inside the `if` condition is evaluated for each number in the list. If the number is greater than zero, it is included in the new list.