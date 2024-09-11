### Flip Case Function in Python
```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The string with case flipped.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])
```

You can use this function by calling `flip_case('Hello')`, which will return `'hELLO'`. 

Note: This function uses a list comprehension to iterate over each character in the string, converting lowercase characters to uppercase and uppercase characters to lowercase. The `join` function is then used to combine the characters back into a single string.