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

This Python script defines the `strlen` function to return the length of a given string. The `len` function is built into Python and can be used to find the length of any sequence (including strings), so it's the most efficient way to solve this problem. 

However, if you were to rewrite this function manually without using the `len` function, it would look something like this:

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
    length = 0
    for _ in string:
        length += 1
    return length
```
This version of the function iterates over each character in the string, incrementing a counter for each character. This method is less efficient than using the `len` function, as it requires a full iteration over the string, but it can be useful if you need to manually implement a function for some reason.