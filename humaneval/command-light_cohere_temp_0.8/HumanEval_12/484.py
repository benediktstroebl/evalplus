```python
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> longest([]) == None
    >>> longer(["a", "bb", "ccc"]) == "ccc"
    >>> longest(["a", "bb", "bb", "ccc"]) == "ccc"
    >>> longest(["a", "bb", "ccc", "a"]) == "a"
    """
    return max(strings, key=len, default=None)
```