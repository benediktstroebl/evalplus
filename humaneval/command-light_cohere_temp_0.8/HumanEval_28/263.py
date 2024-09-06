```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', ' ', 'b', 'c'])
    'abc '
    >>> concatenate(['a', 'b', 'c', 'd'])
    'abc d'
    >>> concatenate([1,2,3])
    Traceback (most recent call last):
    TypeError: input must be iterable, not int64(3)
    """
    if not strings:
        return ""
    return "".join("".join(strings))
```