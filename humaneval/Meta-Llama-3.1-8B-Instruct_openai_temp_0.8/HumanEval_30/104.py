```python
def get_positive(l: list):
    """
    Return only positive numbers in the list.

    Args:
        l (list): A list of numbers.

    Returns:
        list: A list of positive numbers from the input list.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in l if num > 0]
```

This script uses a list comprehension to create a new list that includes only the numbers from the input list that are greater than 0, which is the definition of a positive number. The function takes a list of numbers as input and returns a new list with the desired numbers.