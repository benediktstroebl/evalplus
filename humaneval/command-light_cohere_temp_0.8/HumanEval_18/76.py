```python
def how_many_times(string: str, substring: str) -> int:
    """
    Returns count of occurrences of the substring in the original string.
    """
    string = "aaaaaaaa"
    sub = "aa"
    return len(string.find(sub))
```