```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'

    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The flipped string.
    """
    return ''.join([char.swapcase() for char in string])

# Test the function
print(flip_case('Hello'))  # Expected output: 'hELLO'
print(flip_case('WORLD'))  # Expected output: 'wOrld'
print(flip_case('Python'))  # Expected output: 'pYTHON'
```

This script defines the `flip_case` function, which utilizes the `swapcase()` string method to flip the case of each character in the input string. The result is then returned as a string. The function is tested with several examples.