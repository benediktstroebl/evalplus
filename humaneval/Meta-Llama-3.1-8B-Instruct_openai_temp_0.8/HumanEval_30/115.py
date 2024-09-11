```python
def get_positive(lst: list):
    """Return only positive numbers in the list.
    
    Args:
    lst (list): A list of integers.

    Returns:
    list: A list of positive integers from the input list.

    Example:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in lst if num > 0]
```

To use this function, you can simply call `get_positive()` with a list of integers as an argument, like this:
```python
numbers = [-1, 2, -4, 5, 6]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [2, 5, 6]
```