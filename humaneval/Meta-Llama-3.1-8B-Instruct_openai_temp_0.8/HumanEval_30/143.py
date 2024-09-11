### Python Script to Get Positive Numbers in a List
```python
def get_positive(lst: list) -> list:
    """
    Return only positive numbers in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        list: A list of positive numbers from the input list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in lst if num > 0]


# Test the function
print(get_positive([-1, 2, -4, 5, 6]))
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```
This Python script uses a list comprehension to create a new list containing only the numbers from the input list that are greater than 0.