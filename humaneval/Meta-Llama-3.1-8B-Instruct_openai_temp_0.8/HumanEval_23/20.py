```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python, which returns the number of items in an object. In the case of a string, `len` returns the number of characters in the string.

You can use this function like this:

```python
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```