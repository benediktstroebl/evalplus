```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of times the substring can be found in the string.
    """
    string = 'aaaaaa'
    sub = 'a'
    return len(string.find(substring))
```