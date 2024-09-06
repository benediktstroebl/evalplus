```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns count of occurrences of the substring in the string, 
    ignoring case and overlapping occurrences.
    """
    using a Python'sre_search function, with a possible 
    match function that can be used with the same parameters.
    """
    pattern, string and substring are  case-insensitive.
    return sum(pattern in string for pattern in substring)
    """
def match(string, sub) -> bool: 
    return string.lower().
    .= sub.lower() and string
 string
return False
```