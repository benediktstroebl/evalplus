```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.swapcase() for char in string])


# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('aBc'))  # Output: 'AbC'
```

This script defines a function `flip_case` that takes a string as input, swaps the case of each character using the `swapcase` method, and returns the resulting string. The test cases at the end demonstrate the function's behavior.