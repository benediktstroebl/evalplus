```python
def strlen(string: str) -> int:
    """ Return length of given string
    
    Args:
    string (str): Input string
    
    Returns:
    int: Length of the input string
    
    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Testing the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('Hello World'))  # Output: 11
```