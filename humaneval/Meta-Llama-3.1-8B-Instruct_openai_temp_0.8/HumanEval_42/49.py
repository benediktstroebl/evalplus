```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list of integers.

    Returns:
        list: List with each element incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]  # Use list comprehension to increment each element by 1
```

This script defines a function `incr_list` that takes a list of integers as input and returns a new list where each element is incremented by 1. It uses list comprehension to achieve this in a concise and efficient manner. The example use cases are included as comments to demonstrate the function's behavior. You can run this script to test the function.