```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of positive numbers from the input list.

    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]
```

This script uses a list comprehension to create a new list that only includes numbers from the input list where the number is greater than 0 (i.e., positive). The `[num for num in numbers if num > 0]` part is equivalent to a for loop that iterates over each number in the input list and checks if it's positive. If it is, the number is added to the new list.