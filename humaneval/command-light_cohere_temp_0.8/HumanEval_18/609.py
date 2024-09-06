```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of times the substring appears anywhere in the original string.
    """ 
    # This guaranteed: 
    - The input strings are valid and don't contain any errors
    - The substring is found anywhere in the string
    """
    return sum(1 for w in string.contains(substring))
```