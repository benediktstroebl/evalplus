```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('''' + 'def')
    6
    >>> strlen('abcde') == len('abcde')
    True
    """
    return len(string)
```