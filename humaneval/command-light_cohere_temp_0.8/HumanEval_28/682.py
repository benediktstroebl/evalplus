```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string, ignoring empty strings.
    >>> s = ['a', 'b', ' ', 'c']
    >>> concatenate(s) == 'abc'
    True
    >>> s = ['', 'a', 'b', 'c']
    >>> concatenate(s) == 'abc'
    True
    >>> s = ['a', 'b', 'c', '']
    >>> concatenate(s) == 'abc'
    True
    >>> s = ['a', ' ', 'b', 'c']
    >>> concatenate(s) == 'abc'
    True
    """
    if not strings:
        return ''
    return ''.join(strings)
```