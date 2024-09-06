```python
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    >>> list of strings has to be non-empty.

    >>> assert longest([]) is None
    >>> assert longest(['a']) is None
    >>> assert longest(['a', 'b']) == 'a'
    >>> assert longest(['a', 'bb', 'ccc']) == 'ccc'

    >>> longest(['abc', 'ab', 'a'])
    'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
```