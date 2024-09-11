```python
def get_positive(numbers: list):
    """
    Filter a list of numbers and return only the positive ones.

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


# Example usage
numbers = [-1, 2, -4, 5, 6]
print(get_positive(numbers))  # Output: [2, 5, 6]

numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(numbers))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

In this script, we define a function `get_positive` that takes a list of numbers as input. It uses a list comprehension to create a new list that only includes numbers greater than 0. We then demonstrate the function's usage with two example lists.