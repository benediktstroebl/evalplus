```python
def get_positive(numbers: list) -> list:
    """
    Returns a list containing only the positive numbers from the input list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of positive integers.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Test the function
numbers1 = [-1, 2, -4, 5, 6]
numbers2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print(get_positive(numbers1))  # Output: [2, 5, 6]
print(get_positive(numbers2))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script uses a list comprehension to create a new list containing only the positive numbers from the input list. The list comprehension iterates over each number in the input list and includes it in the output list if it is greater than 0.