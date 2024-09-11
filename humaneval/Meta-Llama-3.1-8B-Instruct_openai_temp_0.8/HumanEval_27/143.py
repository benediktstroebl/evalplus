```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The flipped string.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return string.swapcase()

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('aBcDe'))  # Output: 'aBcDe'
```