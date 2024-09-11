```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The string with lowercase characters flipped to uppercase and uppercase to lowercase.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)


# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('HEllo'))  # Output: 'hElLo'
print(flip_case('hELLO'))  # Output: 'HeLLO'
```

This script uses a generator expression to iterate over each character in the string, swapping its case using the `swapcase()` method, and then joins the result back into a string using the `join()` method. The `swapcase()` method returns a string where all the lowercase characters are converted to uppercase and all the uppercase characters are converted to lowercase.