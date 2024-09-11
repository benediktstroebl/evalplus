### String Length Function
#### A Python Function to Calculate the Length of a Given String
```python
def strlen(string: str) -> int:
    """Return the length of the given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Example:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```
This function uses the built-in `len()` function in Python to calculate the length of the given string. It takes a string as input and returns its length as an integer. The docstring explains the purpose of the function, its input argument, and its return value, along with some example usage.