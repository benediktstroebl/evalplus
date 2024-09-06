```python
def strlen(string: str) -> int:
    """ Returns the length of a string. 
    NOTE: This function accepts both strings and NoneType, 
    and returns 0 for NoneType input. """
    if string is None:  return 0
    return len(string)
```