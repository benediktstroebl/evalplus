```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            AttributeError: 'str' object does not support attribute '__len'`
        """
    return len(string)
```