### Increment List Elements
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list of integers.

    Returns:
        list: The list with all elements incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]
```
This script uses a list comprehension to create a new list where each element is the corresponding element in the input list incremented by 1. The type hint for the function parameters and return value indicate that the function expects a list and returns a list, and that the list contains integers. The docstring provides a description of the function, its parameters, and its return value, as well as some examples of how to use it.