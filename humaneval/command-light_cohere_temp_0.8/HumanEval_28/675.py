```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> strings = ['the', 'is', 'a nice', 'foo']
    >>> concatenate(strings)
    'theisannisffoo'
    """
    return ''.join(''.join(strings) if strings else '')
```