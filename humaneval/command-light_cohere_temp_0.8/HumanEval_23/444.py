```python
def strlen(string: str) -> int:
    """ Return length of given string
    Returns length of string if it's not empty, otherwise returns 0 """
    if not string:
        return 0
    return len(string)
```