Here is a Python script that solves the problem:
```python
def get_positive(numbers: list) -> list:
    """Return only positive numbers in the list.

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

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123, 1]
```
This script uses a list comprehension to filter the input list for positive numbers. The `if num > 0` condition is used to select only the positive numbers from the list. The result is then returned as a new list.