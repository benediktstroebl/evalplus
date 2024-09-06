```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('')
    Traceback (most recent call last):
      File "<string>", line 4, in strlen()
        raise ValueError("Input string cannot be empty")
    """
    if not string:
        raise ValueError("Input string cannot be empty")
    return len(string)
```