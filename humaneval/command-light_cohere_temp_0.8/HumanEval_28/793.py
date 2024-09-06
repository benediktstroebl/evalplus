```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', ''])
    'abc'
    >>> concatenate(['a', 'b', '', 'c'])
    'abc'
    """
    return ''.join(strings, sep='')
```