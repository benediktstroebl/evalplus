```python
def get_positive(numbers: list):
    """
    Returns a list of only positive numbers from the input list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of only positive numbers.

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

This Python script defines a function called `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the original list. The function uses a list comprehension to iterate over the input list and include only the numbers that are greater than zero. The script also includes docstrings to document the function's behavior and provide examples of how to use it.