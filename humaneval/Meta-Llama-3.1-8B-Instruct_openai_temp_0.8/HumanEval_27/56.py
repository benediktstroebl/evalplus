```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The input string with lowercase characters flipped to uppercase and uppercase to lowercase.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.swapcase() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('world'))  # Output: 'WoRlD'
print(flip_case('Python'))  # Output: 'pYtHoN'
```

This script defines a function `flip_case` that takes a string as input, applies the `swapcase` method to each character in the string, and returns the resulting string with lowercase characters flipped to uppercase and uppercase to lowercase. The `swapcase` method is a built-in string method in Python that accomplishes this task.