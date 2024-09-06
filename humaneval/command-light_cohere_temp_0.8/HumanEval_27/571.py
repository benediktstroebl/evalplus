```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    Args: 
        string (str): the string to flip the case of
    Returns: 
        string with all characters flipped.
    """

# tests
    assert flip_case('hello') == 'olleH'
    assert flip_case('HEllO') == 'olleO'
```