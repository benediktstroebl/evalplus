```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hello'))  # Output: 'HELLO'
```

This script defines a function `flip_case` that takes a string as input and returns a new string with the case of each character flipped. It uses a generator expression to iterate over each character in the input string, and for each character, it checks whether the character is lowercase using the `islower` method. If the character is lowercase, it converts it to uppercase; otherwise, it converts it to lowercase. The resulting string is then returned by the function.