```python
def get_positive(numbers: list) -> list:
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of only the positive numbers from the input list.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This Python script defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. The function uses a list comprehension to create the new list, iterating over the input list and including a number in the new list only if it is greater than 0. The script then tests the function with two example inputs, printing the results to the console.