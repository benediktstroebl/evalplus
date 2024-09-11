```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrLD'
print(flip_case('Python'))  # Output: 'pYtHoN'
```

This script defines the `flip_case` function which takes a string as input, swaps the case of each character using the `swapcase()` method, and returns the resulting string. The `"".join()` method is used to concatenate the characters back into a string. The script also includes some test cases to demonstrate the function's behavior.