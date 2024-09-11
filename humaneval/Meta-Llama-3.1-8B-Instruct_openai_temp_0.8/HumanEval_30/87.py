```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
    numbers (list): A list of numbers.

    Returns:
    list: A list of positive numbers.

    Example:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Example usage:
numbers1 = [-1, 2, -4, 5, 6]
numbers2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print(get_positive(numbers1))  # Output: [2, 5, 6]
print(get_positive(numbers2))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script uses list comprehension to create a new list that includes only the numbers from the input list that are greater than zero. The `get_positive` function is then called with two different lists of numbers to demonstrate its usage.