Here's a Python script that solves the problem:

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
numbers = [-1, 2, -4, 5, 6]
print(get_positive(numbers))  # Output: [2, 5, 6]

numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(numbers))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script uses a list comprehension to filter out non-positive numbers from the input list. The `list` is iterated over and each number is checked if it's greater than 0. If it is, the number is included in the resulting list.