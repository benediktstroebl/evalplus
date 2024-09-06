```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Return the count of occurrences of a given substring within the original string.
    """ 
    A count of 1 is returned if the substring is empty or not found. 
    """
    string = "aaaaaa"
    sub = "a"
    return len(string.find(sub))
```