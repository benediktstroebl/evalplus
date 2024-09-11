### Flip Case of a String
```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with lowercase characters converted to uppercase and vice versa.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)
```

You can run this script in a Python environment to test the `flip_case` function. This function uses a generator expression to iterate over each character in the input string. If a character is lowercase, it is converted to uppercase; otherwise, it is converted to lowercase. The `join` method is used to concatenate the modified characters back into a single string.