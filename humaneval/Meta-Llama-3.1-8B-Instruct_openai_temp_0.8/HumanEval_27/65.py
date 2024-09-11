```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string

    Returns:
        str: The string with case flipped

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))
print(flip_case('Hello World'))
```

In this script, we define a function `flip_case` that takes a string as input. It uses a generator expression to iterate over each character `c` in the input string. The `swapcase()` method is used to flip the case of each character, and the resulting characters are joined back together into a string using `''.join(...)`.