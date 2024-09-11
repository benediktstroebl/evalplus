```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with case flipped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('123'))    # Output: '123' (no case change for digits and special characters)
```
In this script, the `flip_case` function uses a list comprehension to iterate over each character in the input string. If the character is uppercase (`isupper()` returns `True`), it converts it to lowercase using `lower()`. If the character is lowercase, it converts it to uppercase using `upper()`. The `''.join()` method is used to concatenate the characters back into a single string.