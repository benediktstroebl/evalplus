```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

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
numbers1 = [-1, 2, -4, 5, 6]
numbers2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print(get_positive(numbers1))  # Output: [2, 5, 6]
print(get_positive(numbers2))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function called `get_positive` that uses a list comprehension to create a new list containing only the positive numbers from the input list. The `if` condition in the list comprehension (`num > 0`) ensures that only positive numbers are included in the output list. The script also includes example usage of the `get_positive` function.