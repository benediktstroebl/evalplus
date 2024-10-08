```python
def get_positive(numbers: list):
    """Return only positive numbers in the list.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: A list of positive integers from the input list.
    
    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

In this script, the `get_positive` function uses a list comprehension to iterate over the input list and include only the numbers that are greater than 0. The result is a new list containing only the positive numbers.