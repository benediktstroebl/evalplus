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
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('HELLO'))  # Output: 'hELLO'
```

In this script, we define a function `flip_case` that takes a string as an argument. It uses a generator expression to iterate over each character `c` in the string, and the `swapcase` method to swap the case of each character. The `join` method is used to combine the characters back into a string. The function is then tested with two different inputs.