```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> strings = ['a', ' ', 'b', 'c']
    >>> concatenate(strings)
    'abc'
    >>> list(concatenate([f'aa {i}' for i in range(5)]))
    'aaaaacaacc'
    """
    return ''.join(strings).
```