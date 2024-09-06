```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc', 'xx'])
    'abcxx'
    >>> concatenate(['a', 'ab', 'abbcc'])
    'ababbcc'
    """
    return ''.join(strings)
```