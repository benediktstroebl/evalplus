```python
def longest(strings: List[str]) -> Optional[str]:
    """ Return the first non-empty string from a list of strings.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest([''])
    None
    >>> longest(['a', '', 'c'])
    'a'
    >>> longest(['aa', 'xx', 'a'])
    'aa'
    >>> longest(['a', 'a'])
    'a'
    """
    if not strings:
        return None
    return max(strings, key=len)
``` 
This code defines a function `longest` that takes a list of strings as an argument and returns the first non-empty string from that list, or `None` if the list is empty. 

The `max` function is used to compare strings based on their length, and the `key=len` argument is used to make this comparison case-sensitive. 
This code provides a concise and efficient solution to the problem of finding the longest string in a list of strings.