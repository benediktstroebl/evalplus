```python
def incr_list(lst: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        lst (list): The input list to be incremented.

    Returns:
        list: The list with elements incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # Use list comprehension to create a new list with elements incremented by 1
    return [x + 1 for x in lst]

# Test the function
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script defines a function `incr_list` that takes a list as input and returns a new list with each element incremented by 1. It uses list comprehension to efficiently create the new list. The function includes a docstring with examples to illustrate its usage. The script also includes test cases to verify the function's correctness.