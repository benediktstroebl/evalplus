```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to flip.

    Returns:
        str: The string with characters flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wORLD'
print(flip_case('Python'))  # Output: 'pYTHON'
```

In this script, the `swapcase()` method is used to flip the case of each character in the string, which is then joined back together into a single string. This method is more efficient and Pythonic than manually swapping the case of each character.