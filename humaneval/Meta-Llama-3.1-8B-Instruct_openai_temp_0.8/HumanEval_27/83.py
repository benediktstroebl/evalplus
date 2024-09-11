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

    return string.swapcase()

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HeLLO'
print(flip_case('HeLLO'))  # Output: 'hELLO'
```

The `swapcase()` method is used to swap the case of every letter in the string. This method is a more efficient and Pythonic way to achieve the desired result.