Here's the solution code:
```python
def flip_case(string):
    """
    Flip lowercase characters to uppercase and vice versa
    Args:
        string (str): Input string
    Returns:
        string (str): String with characters flipped.
    """
    return string.handle_lowercase(string.handle_upper(string))
```

The function `flip_case` takes a string as input and returns a string with the characters flipped. The function `handle_lower` and `handle_upper` handle the input string to flip the case of the characters, respectively.

Note: The function `handle_lower` takes an input string and returns a string with all the lowercase characters of it converted to uppercase, and vice versa.