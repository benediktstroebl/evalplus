```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.
    
    Args:
    numbers (list): A list containing integers.
    
    Returns:
    list: A list of positive integers from the input list.
    
    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Example usage:
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that takes a list of numbers as input. It uses a list comprehension to create a new list containing only the positive numbers from the input list. The function then returns this new list. The script includes docstrings and example usage to demonstrate how to use the function.