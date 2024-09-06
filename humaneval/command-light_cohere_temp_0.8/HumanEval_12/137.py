```python
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the length of the longest string.

    >>> str longest('abc')
    >>> longest(['abc'])
    6
    >>> longest(['abc', 'abc'])
    ... (undefined)
    >>> longest(['abc', 'abc', 'abc'])
    6
    >>> longest([])
    ... (undefined)
    >>> longest(['aa', ''])
    Traceback (most recent call last):
      File "<stdin>", line 12, line 1:
       TypeError: 'list' object does not support item assignment
    """
    if not strings:
        return None
    return max(strings, key=len)
```
The provided code solves the following problem: Given a list of strings, it finds the length of the longest string in the list. It returns the maximum length if multiple strings of the same length, and returns None in case of an empty list.