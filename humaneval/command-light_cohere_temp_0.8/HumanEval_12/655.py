```python
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string in the list.
    >>> longest(['a', 'b', 'c']) == 'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
```