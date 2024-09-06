```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcde')
        5
        >>> strlen('')
        Traceback (most recent call last):
          File "<filename>", line 3, in strlen()
            ^
        File "<stdin>", line expected '>' but got '' instead.
        File "<ip",utf8", first line of traceback (an error).
    """
    return len(string)
```