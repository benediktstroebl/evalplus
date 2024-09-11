### Length of a String
```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```
This script defines a function `strlen` that takes a string as input and returns its length. The `len` function in Python is used to get the length of a string. The docstring explains how to use the function and provides examples of its usage.

To run the script, save it to a file (for example, `strlen.py`) and execute it with Python (for example, `python strlen.py`). You can then test the function with the example usage shown in the docstring.