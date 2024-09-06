```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string.
    Example the string and substring to search for.
    Returns: number of times they substring occurs.
    """
    string = 'aaaa'
    substring = 'aa'
    return len(string.find(substring))
```