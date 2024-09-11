```python
def get_positive(numbers: list) -> list:
    """
    Return a list of only positive numbers from the input list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        list: A list of positive numbers.
    
    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```

This Python script uses list comprehension to filter out the positive numbers from the input list. It defines a function `get_positive` that takes a list of numbers and returns a new list containing only the positive numbers. The function includes docstrings and example usage to demonstrate its functionality.