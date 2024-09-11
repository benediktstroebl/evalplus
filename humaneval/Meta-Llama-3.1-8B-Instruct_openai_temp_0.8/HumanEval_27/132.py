```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip the case.

    Returns:
        str: The string with case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])
```

This script defines a function `flip_case` that takes a string as input and returns a new string with its case flipped. The function uses list comprehension to iterate over each character in the string, converts it to uppercase if it's lowercase and vice versa, and joins the characters back into a string using the `join` method.