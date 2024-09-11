```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string to be flipped.

    Returns:
    str: The string with all lowercase characters flipped to uppercase and all uppercase characters flipped to lowercase.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('Hello World'))  # Output: 'hELLO wORLD'
```

This script defines a function `flip_case` that takes a string as input and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. The function uses a generator expression to iterate over each character in the string, swap its case using the `swapcase` method, and join the resulting characters back into a string.