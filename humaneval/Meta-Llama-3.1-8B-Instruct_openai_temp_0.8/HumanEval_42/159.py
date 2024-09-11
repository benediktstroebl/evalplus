```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The list of numbers to increment.

    Returns:
        list: The list with elements incremented by 1.
    """
    return [x + 1 for x in l]

# Test the function
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This Python script defines a function `incr_list` that takes a list of numbers and returns a new list with each number incremented by 1. It uses a list comprehension for efficient and readable code. The test cases at the end of the script demonstrate its usage.