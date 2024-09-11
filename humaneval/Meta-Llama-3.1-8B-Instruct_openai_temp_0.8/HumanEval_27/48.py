```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Test the function
print(flip_case('Hello'))  # Expected output: hELLO
print(flip_case('WORLD'))  # Expected output: wOrld
print(flip_case('Python'))  # Expected output: pYTHON
```

This script uses a list comprehension to iterate over each character in the input string. If the character is lowercase, it converts it to uppercase; otherwise, it converts it to lowercase. The `join()` function is used to concatenate the characters back into a string.