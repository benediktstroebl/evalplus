```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The string with case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.swapcase() for char in string)
```

In this code:

- The `swapcase()` method is used to swap the case of each character in the string.
- The generator expression `(char.swapcase() for char in string)` is used to create a new string where each character's case has been swapped.
- The `''.join(...)` method is then used to join all the characters back together into a single string.