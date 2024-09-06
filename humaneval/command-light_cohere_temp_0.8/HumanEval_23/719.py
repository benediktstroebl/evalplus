Here is a Python script with a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
      File "<string>", line 6, in strlen()
        raise ValueError('Input string is empty')
    ValueError: Input string is empty
    """
    if not string:
        raise ValueError('Input string is empty')
    return len(string)
```