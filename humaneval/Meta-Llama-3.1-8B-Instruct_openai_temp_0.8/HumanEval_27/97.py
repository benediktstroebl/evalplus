```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string to be flipped.

    Returns:
    str: The flipped string.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.swapcase() for char in string])

# Test the function
print(flip_case('Hello'))
print(flip_case('hELLO'))
print(flip_case('123ABC'))
```

This script defines a function `flip_case` that takes a string as input, swaps the case of each character using the `swapcase()` method, and returns the resulting string. The script then tests the function with a few examples.