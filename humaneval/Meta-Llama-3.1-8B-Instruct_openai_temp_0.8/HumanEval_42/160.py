```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list.

    Returns:
        list: The list with elements incremented by 1.
    """
    # Use list comprehension to create a new list with elements incremented by 1
    return [x + 1 for x in l]

# Test cases
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. It uses list comprehension, a concise way to create a new list from an existing list by applying a function to each element. The script then includes test cases to verify that the function behaves as expected.