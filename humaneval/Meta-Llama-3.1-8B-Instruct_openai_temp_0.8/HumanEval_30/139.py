```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of positive numbers from the input list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Example use case
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(numbers))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that filters a list of numbers to include only positive numbers. It uses a list comprehension to create a new list that includes only the numbers from the input list that are greater than zero. The function is then tested with an example list of numbers.