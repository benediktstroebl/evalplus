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

# Test the function
numbers1 = [-1, 2, -4, 5, 6]
numbers2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print(get_positive(numbers1))  # Expected output: [2, 5, 6]
print(get_positive(numbers2))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function called `get_positive` which takes a list of numbers as input and returns a new list containing only the positive numbers from the original list. It uses a list comprehension to create the new list, which is an efficient and concise way to create lists in Python. The function is then tested with two example lists to demonstrate its usage.