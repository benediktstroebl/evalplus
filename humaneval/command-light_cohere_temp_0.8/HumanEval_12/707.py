```python
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    >>> list(['a', 'bb', 'ccc']) 
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'

    >>> list('abc') != longest(['a', 'bb', 'ccc'])
    True

    >>> strings = ['apple', 'app', 'a', 'pie', 'orange']
    >>> longest(strings)
    'apple'

    >>> longest(['abc'])
    'abc'
    """

    # type checking
    if not isinstance(strings, list):
        raise TypeError("Input should be a list")

    # check empty list
    if not strings:
        return None

    # sort the list
    strings.sort()

    # determine the reason is the list
    return max(strings, key=len)
```