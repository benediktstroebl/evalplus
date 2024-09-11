```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string to flip case.

    Returns:
    str: The input string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hello'))  # Output: 'HELLO'
print(flip_case('HeLlO'))  # Output: 'hELLO'
```

This script uses the built-in string method `swapcase()` to swap the case of each character in the string. The `join()` method is used to concatenate the characters back into a single string.