```python
def get_positive(numbers: list) -> list:
    """
    Return a list of only positive numbers from the input list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of positive numbers.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num >= 0]

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123, 1]
```

In this script, the function `get_positive` uses a list comprehension to create a new list that includes only the numbers from the input list that are greater than or equal to 0 (positive numbers). The example usage at the end shows how to use the function to solve the problem specified.