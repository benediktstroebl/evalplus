```python
def concatenate(strings: List[str]) -> str:
    """
    Returns the concatenation of all strings in the input list.
    >>> strings = ['a', 'b', 'c']
    >>> concatenate(strings)
    'abc'
    >>> strings = []
    >>> concatenate(strings)
    ''
    >>> strings = ['a', 'b', 'c']
    >>> strings[0] = 'X'
    >>> concatenate(strings)
    'Xabc'
    """
    return ''.join(strings)
```