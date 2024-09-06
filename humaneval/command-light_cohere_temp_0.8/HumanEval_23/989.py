```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
             File "<filename>", line 9, in strlen()
             File "<ipython file>", line 3, in function
                ...
                raise ValueError('input is not a string')
    """
    if not isinstance(string, str):
        raise ValueError('input is not a string')
    return len(string)
```