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
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HELLO'
print(flip_case('HeLlO'))  # Output: 'hELLO'
```

In this script, the `flip_case` function uses a generator expression to iterate over each character in the input string. The `swapcase` method is used to flip the case of each character. Finally, the `join` method is used to concatenate the characters back into a string.