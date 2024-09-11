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


# Test the function
print(flip_case('Hello'))  # hELLO
print(flip_case('WORLD'))  # wOrld
```

This script uses the built-in `swapcase()` method in Python, which swaps the case of all characters in a string. The `join()` method is then used to combine the swapped characters back into a string.