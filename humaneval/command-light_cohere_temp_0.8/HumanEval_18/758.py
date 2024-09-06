```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string, 
    while ignoring case and counting overlapping substrings.
    >>> 'a'
    string = 'hello world'
    >>> 'a' 
    0
    >>> 'A' 
    1
    >>> 'aAA' 
    2
    >>> 'Aa' 
    2
    >>> 'aaaa' 
    3
    >>> 'aaaaaa'
    0
    """
    return _count_recursive(string, substring, 0)

def _count_recursive(string: str, substring: str, count: int) -> int:
    """
    Check if the substring is found, and return its count. If not found, 
    return the count + 1.
    """
    if substring == string[0:]:
        return count
    if substring[0] == string[0]:
        return _count_recursive(string[1:], substring[1:], count + 1)
    return _count_recursive(string[1:], substring, count)
```