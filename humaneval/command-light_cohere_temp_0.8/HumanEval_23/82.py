```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
             File "<filename>", line 1, in strlen()
             File "<ipython file>", line 20, in function '__main__':
                raise ValueError('Invalid string')
    """
    if not string:
        return 0
    return len(string)
```