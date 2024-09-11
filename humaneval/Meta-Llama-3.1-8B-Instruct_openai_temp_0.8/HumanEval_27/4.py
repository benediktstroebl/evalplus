```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with flipped case.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.swapcase() for char in string)
```

This function uses a generator expression to iterate over each character in the string, swaps its case using the `swapcase` method, and then joins all the characters back into a string using `''.join()`. The `swapcase` method returns the uppercase version of a lowercase character and the lowercase version of an uppercase character, effectively flipping the case.

You can test this function with different inputs to see how it works.