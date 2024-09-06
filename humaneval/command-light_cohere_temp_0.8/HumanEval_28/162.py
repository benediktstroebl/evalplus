```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> strings = ['a', 'b', 'c', 'd']
    >>> concatenate(strings)
    'abcd'
    """
    return ''.join(s for s in strings)
```