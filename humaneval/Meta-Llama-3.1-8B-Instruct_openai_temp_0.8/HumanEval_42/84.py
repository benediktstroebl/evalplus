```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1.

    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # Use list comprehension to create a new list with elements incremented by 1
    return [element + 1 for element in l]


# Example usage
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that takes a list of elements as input and returns a new list where each element is incremented by 1. It uses list comprehension to create the new list, which is a concise and efficient way to perform this operation. The example usage demonstrates how to use the function with different input lists.