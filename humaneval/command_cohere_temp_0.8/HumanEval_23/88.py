```python
def strlen(string: str) -> int:
    """ Returns the length of a string """
    return len(string)
```
This Python function uses the built-in `len()` method to return the number of characters in the provided string. It correctly handles any string input, including empty strings, and will yield a `TypeError` if an invalid type is given.