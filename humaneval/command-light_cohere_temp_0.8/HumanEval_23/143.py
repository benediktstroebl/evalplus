```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('!")
        2
        >>> strlen('')
        Traceback (most recent call last):
            TypeError: 'string' object does not support item assignment
            """
    return len(string)
```