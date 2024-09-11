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

This Python script defines a function `strlen` that takes a string as input and returns its length. The length of a string is calculated using the built-in `len` function in Python, which returns the number of items in an object. In the case of a string, it returns the number of characters.

To use this function, you can call it with a string as an argument, like this:
```python
print(strlen('hello'))  # Output: 5
print(strlen('world'))  # Output: 5
```