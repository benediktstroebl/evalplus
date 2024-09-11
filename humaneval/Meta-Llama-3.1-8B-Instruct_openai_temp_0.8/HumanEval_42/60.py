```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1.

    Args:
        l (list): The input list of integers.

    Returns:
        list: The list with all elements incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]
```

This script defines a function `incr_list` that takes a list of integers as input and returns a new list where each element is incremented by 1. The function uses a list comprehension to achieve this in a concise and efficient manner. 

The function includes a docstring that provides a description of what the function does, lists the function's parameters and return values, and includes examples of how to use the function. 

You can save this script to a file (e.g., `incr_list.py`) and run it from the command line to test the function. For example:
```bash
$ python incr_list.py
```