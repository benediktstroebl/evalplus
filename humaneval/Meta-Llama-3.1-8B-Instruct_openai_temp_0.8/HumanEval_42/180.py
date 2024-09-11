```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
    l (list): List of numbers to be incremented.

    Returns:
    list: List with elements incremented by 1.
    """
    return [i + 1 for i in l]

# Test cases
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script uses a list comprehension to create a new list where each element is the corresponding element in the input list incremented by 1. The test cases at the end show the function's usage and demonstrate its correctness.