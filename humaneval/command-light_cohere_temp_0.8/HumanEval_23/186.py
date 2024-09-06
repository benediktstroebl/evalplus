```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            AttributeError: 'function__dict' object has no attribute '__dict__'
    """
    return len(string)
```