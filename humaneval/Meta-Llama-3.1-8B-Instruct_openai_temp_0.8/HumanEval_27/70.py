### Flip Case Function
```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string.
    
    Returns:
    str: The string with flipped case.
    
    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()
```

### Example Usage
```python
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('Hello World'))  # Output: 'hELLO wORLD'
```

Note: The `swapcase()` method is a built-in string method in Python that does the same thing as the `flip_case()` function. This script uses this method to make the code concise and more Pythonic. If you want to implement the logic from scratch, here is an alternative version:

```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string.
    
    Returns:
    str: The string with flipped case.
    
    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result
```