```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
    l (list): List of numbers.

    Returns:
    list: List with elements incremented by 1.
    """
    return [x + 1 for x in l]

# Test the function
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

In this script, we use a list comprehension to increment each element in the input list `l` by 1. The expression `x + 1` calculates the incremented value for each element `x` in the list, and the resulting values are collected into a new list, which is then returned by the function.