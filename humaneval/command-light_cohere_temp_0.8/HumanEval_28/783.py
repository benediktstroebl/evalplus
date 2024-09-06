```python
def concatenate(strings: List[str]) -> str:
    """
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'b', 'c', 'd'])
    'abcd'
    """
    return ''.join(strings)
```