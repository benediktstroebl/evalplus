### Flip Case Function
```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string to flip case.

    Returns:
    str: The input string with case flipped.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])
```

### Example Usage
```python
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('wORLD'))  # Output: 'WoRlD'
print(flip_case('Python'))  # Output: 'pYtHoN'
```

This function uses a list comprehension to iterate over each character in the input string. For each character, it checks if the character is lowercase using the `islower()` method. If it is, it converts it to uppercase using the `upper()` method. If it is not (i.e., it's uppercase), it converts it to lowercase using the `lower()` method. The resulting list of characters is then joined back into a string using the `join()` method.