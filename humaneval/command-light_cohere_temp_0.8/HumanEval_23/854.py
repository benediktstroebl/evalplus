```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcabc')
        5
        >>> strlen('') | "" == 0
        True
        >>> str.split('abc') == ['a', 'b', 'c']
        True
    """
    return len(string)
```