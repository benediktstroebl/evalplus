```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string to flip cases.
    
    Returns:
    str: The string with lowercase characters flipped to uppercase and uppercase to lowercase.
    
    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.swapcase() for char in string)
```

In this script, the `swapcase()` method is used to swap the case of each character in the string. This method is a string method in Python that returns a string where each character is swapped to its opposite case. The `join()` method is used to concatenate the characters into a single string.