```python
def get_positive(numbers: list):
    """
    Return a list of only positive numbers from the input list.

    Args:
        numbers (list): A list of numbers that may contain positive, negative, or zero values.

    Returns:
        list: A list of only positive numbers from the input list.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Example usage:
numbers = [-1, 2, -4, 5, 6]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [2, 5, 6]

numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that uses a list comprehension to filter out non-positive numbers from the input list. It then demonstrates the function's usage with two example lists of numbers.