```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            __main__().
        File "<stdin>", line 7
        TypeError: unhashable operand: '>'
    """
    return len(string)
```