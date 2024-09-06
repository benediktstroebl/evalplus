```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(*strings)
```

This function takes a list of strings as input and returns the concatenated string. It uses the string's built-in function 'join(*strings)', which concatenates all the strings in the list into a single string.