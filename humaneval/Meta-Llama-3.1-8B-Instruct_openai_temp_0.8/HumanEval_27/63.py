```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with flipped case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('wORLD'))  # Output: 'WoRlD'
```

This script uses the built-in `swapcase()` method of the string class, which flips the case of each character in the string. The `join()` method is used to concatenate the swapped characters back into a single string.