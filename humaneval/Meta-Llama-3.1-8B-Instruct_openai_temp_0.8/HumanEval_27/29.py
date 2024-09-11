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
    return ''.join([char.swapcase() for char in string])
```

This script uses a list comprehension to iterate over each character in the string, swap its case with `char.swapcase()`, and then join the characters back into a string. This approach is concise and efficient for small strings.