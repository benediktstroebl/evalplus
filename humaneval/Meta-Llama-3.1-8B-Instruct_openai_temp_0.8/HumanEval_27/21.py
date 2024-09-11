```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The string with flipped case.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hello'))  # Output: 'HELLO'
```

This Python script defines a function called `flip_case` that takes a string as input and returns a new string with the characters flipped from lowercase to uppercase and vice versa. The function uses the `swapcase()` method of string objects to achieve this, and the `join()` method to combine the modified characters back into a single string.