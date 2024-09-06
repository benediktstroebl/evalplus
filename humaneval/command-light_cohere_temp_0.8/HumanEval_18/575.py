Here's the solution:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, considering case-insensitive and overlapping matches.
    >>> how_many_times('aaa', 'a') -> 3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    import re
    pattern = re.compile(sub(r'(%s)+|\1', r'\1', substring))
    matches = len(pattern.search(string))
    return matches
```

This function uses the `re.compile()` function to create a case-insensitive regular expression pattern to match the substring against the original string. 

The regular expression `sub()` function is used to remove the matched substring from the original string, and then the `len()` function is used to count the number of matches. 

The function returns the number of times the substring appears in the original string.