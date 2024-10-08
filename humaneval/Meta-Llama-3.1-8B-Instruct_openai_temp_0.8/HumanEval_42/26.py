Here's a Python function to increment each element in a list by 1:
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): A list of integers.

    Returns:
        list: The input list with each element incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]

# Test the function
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script uses list comprehension to create a new list with each element incremented by 1. It's a concise and readable way to perform the task.