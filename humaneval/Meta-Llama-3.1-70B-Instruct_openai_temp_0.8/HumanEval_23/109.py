```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

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

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3
print("All test cases pass.")
```

However, the built-in `len` function in Python already does this. The above function is redundant unless you're trying to implement it manually, in which case it would be more like this:

```python
def manual_strlen(string: str) -> int:
    """
    Return the length of a given string manually.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
        >>> manual_strlen('')
        0
        >>> manual_strlen('abc')
        3
    """
    length = 0
    for _ in string:
        length += 1
    return length

# Test cases
assert manual_strlen('') == 0
assert manual_strlen('abc') == 3
print("All test cases pass.")
```

This version of the function counts the characters in the string manually, rather than relying on the built-in `len` function.