```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with characters flipped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)
```

In this script, we use a generator expression within the `join()` function to iterate over each character `c` in the input string. We use the `islower()` method to check if each character is lowercase, and if so, we convert it to uppercase with `upper()`. Otherwise, we leave the character as is by using `lower()`. The resulting characters are then joined back into a string, which is returned as the result of the `flip_case()` function.