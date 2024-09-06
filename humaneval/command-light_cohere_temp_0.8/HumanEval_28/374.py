```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate([('a'), ('b'), ('c')])
    'abc'
    """
    return ''.join(''.join(strings)
```