```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc'])
    'abc'
    >>> concatenate([''])
    ''
    >>> concatenate(['a', ' ', 'b'])
    'ab'
    >>> concatenate([None, 'a'])
    'a'
    """
    result = ''.join(''.join(strings)
    return result
```