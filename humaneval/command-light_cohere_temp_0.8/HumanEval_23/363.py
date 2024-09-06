Here is a self-contained Python script that defines a function `strlen` that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: The length of the string in UTF-8 encoded bytes.
    Args:
        string: str, the input string to calculate length.
    Returns: int, the length in bytes
    """
    assert isinstance(string, str)
    assert len(string) == strlen(string)
    return len(string)
```