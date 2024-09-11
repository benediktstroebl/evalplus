```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))
```

This script defines a function `flip_case` that uses the `swapcase` method of Python strings to flip the case of each character in the string. The `join` method is used to combine the swapped characters into a single string. The script also includes a test case to demonstrate the function's behavior.