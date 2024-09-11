```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The string with its case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.swapcase() for char in string])

# Test the function
print(flip_case('Hello'))  # Expected output: hELLO
print(flip_case('Hello World'))  # Expected output: hELLO wORLD
```

This script uses a list comprehension to iterate over each character in the input string, and the `swapcase()` method to flip its case. The `join()` method is then used to concatenate the characters back into a string.