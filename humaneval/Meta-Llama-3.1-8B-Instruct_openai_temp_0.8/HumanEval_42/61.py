```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list of integers.

    Returns:
        list: The list with elements incremented by 1.
    """
    return [x + 1 for x in l]

# Test cases
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

In this script, the `incr_list` function uses a list comprehension to create a new list where each element is the corresponding element in the input list incremented by 1. The test cases at the end demonstrate the function's usage.