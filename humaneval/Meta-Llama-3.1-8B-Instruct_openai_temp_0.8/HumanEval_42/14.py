```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): A list of numbers to be incremented.

    Returns:
        list: The list with elements incremented by 1.
    """
    return [i + 1 for i in l]

# Test cases
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This Python script defines a function `incr_list` that takes a list of numbers as input, creates a new list with each element incremented by 1 using a list comprehension, and returns the resulting list. The test cases demonstrate the function's behavior with two different input lists.