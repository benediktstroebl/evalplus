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
    return ''.join(char.swapcase() for char in string)

# Testing the function
print(flip_case('Hello'))  # Output: 'hELLO'
```

In this script, the `swapcase()` method of Python strings is used to swap the case of each character in the string. This method flips the case of each character, meaning that lowercase characters are converted to uppercase and vice versa. The `join()` method is then used to concatenate the swapped characters back into a single string.