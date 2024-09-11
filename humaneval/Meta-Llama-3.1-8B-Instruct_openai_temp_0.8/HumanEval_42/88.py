```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list

    Returns:
        list: List with elements incremented by 1

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # Use list comprehension to create a new list with incremented elements
    return [x + 1 for x in l]
```

This script is self-contained and includes docstrings to provide documentation for the `incr_list` function. You can save this script to a file (e.g., `incr_list.py`) and run it from the command line using `python incr_list.py` to test the function.