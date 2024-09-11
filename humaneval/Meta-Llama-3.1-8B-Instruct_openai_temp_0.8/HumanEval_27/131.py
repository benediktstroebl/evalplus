```python
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The string to flip case.
    
    Returns:
        str: The flipped case string.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.swapcase() for c in string)
```

This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. The `swapcase()` method is used to swap the case of each character in the string. The `join()` method is used to combine the swapped characters back into a single string.