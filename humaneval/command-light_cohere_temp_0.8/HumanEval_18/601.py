```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count all occurrences of a substring within the original string.
    Returns the method uses a string to find all occurrences of the substring.
    Returns -1 if substring not found, else returns count.
    """
    string:str
    substring:str
    """
    if substring not in string:
        return -1
    return len(string.find(substring))
```