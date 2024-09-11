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
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('HeLlO'))  # Output: 'hElLo'
```

This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. The `swapcase` method is used to swap the case of each character in the string. The `join` method is used to concatenate the characters back into a string. The script also includes some test cases to demonstrate the function's behavior.