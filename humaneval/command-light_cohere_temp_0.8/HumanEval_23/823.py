```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns: The length of the string in Unicode code units.
        Raises: ValueError if the string is None."""
    if not string:
        raise ValueError("Input string is None")
    return len(string)
```