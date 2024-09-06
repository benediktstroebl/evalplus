```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('hello world')
    11
    >>> strlen('   ')
    4
    >>> str.len('')
    strings = ['abc', 'abc123', 'abc')
    for s in strings:
        assert strlen(s) == 3, f'{s} should have length 3'
    return len(string)
```