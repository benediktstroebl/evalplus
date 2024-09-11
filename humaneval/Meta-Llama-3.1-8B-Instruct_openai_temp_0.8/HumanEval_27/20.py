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
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result

# Test the function
print(flip_case('Hello'))  # Should print 'hELLO'
print(flip_case('hELLO'))  # Should print 'HELLO'
print(flip_case('HelloWorld'))  # Should print 'hELLOwORld'
```

In this script, we define a function `flip_case` that takes a string as input and returns a new string with the case flipped. We use the `islower` method to check if a character is lowercase, and if so, we convert it to uppercase using the `upper` method. If the character is not lowercase (i.e., it's uppercase), we convert it to lowercase using the `lower` method. We then combine the results into a new string and return it.