```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The string to be modified.

    Returns:
        str: The modified string with flipped case.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hello'))  # Output: 'HELLO'
```

This script uses Python's built-in string method `swapcase()` to flip the case of each character in the string. The `join()` function is used to concatenate the modified characters back into a string.