```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<filename>", line 1, in strlen
        ValueError: unbound variable 'string'
    """
    string = str(string)  # Raise error for unbound variable
    return len(string)
```