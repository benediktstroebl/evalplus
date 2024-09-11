```python
def get_positive(numbers: list):
    """
    Filter a list to include only positive numbers.
    
    Args:
    numbers: A list of numbers.
    
    Returns:
    A list of positive numbers from the input list.
    
    Example:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Testing the function
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This Python script uses a list comprehension to filter out non-positive numbers from the input list. It returns a new list that includes only positive numbers. The `if num > 0` condition inside the list comprehension ensures that only numbers greater than zero are included in the output list.