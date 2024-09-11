```python
def incr_list(lst: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        lst (list): The input list of integers.

    Returns:
        list: The list with all elements incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in lst]
```

To use this function, you can save it in a Python file (e.g. `incr_list.py`) and run it with Python. For example:

```bash
$ python incr_list.py
```

Then, you can call the function with a list of integers:

```python
>>> from incr_list import incr_list
>>> lst = [1, 2, 3]
>>> incr_list(lst)
[2, 3, 4]
```

You can also use the function directly without importing it:

```python
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```