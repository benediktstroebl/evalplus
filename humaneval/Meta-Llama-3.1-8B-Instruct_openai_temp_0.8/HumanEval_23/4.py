```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Parameters:
    string (str): The input string
    
    Returns:
    int: The length of the input string
    
    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('Hello, World!'))  # Output: 13
```