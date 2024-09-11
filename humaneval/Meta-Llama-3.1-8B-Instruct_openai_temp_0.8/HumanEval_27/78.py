```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip the case.

    Returns:
        str: The string with flipped case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('WORLD'))  # Output: wOrld
```

In this script, we use the `swapcase()` method of the string class, which swaps the case of each character in the string. The `''.join(...)` expression is used to concatenate the characters back into a single string. This approach avoids creating intermediate strings and is more memory-efficient.