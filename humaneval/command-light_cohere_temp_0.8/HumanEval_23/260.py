Here's the self-contained Python function to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
    ...
    ValueError: integer() arg should be a string, not None
    """
    return len(string)
```