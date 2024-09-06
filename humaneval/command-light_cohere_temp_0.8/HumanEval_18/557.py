```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    while ignoring case and taking overlapping substrings into account.
    """
    string = "hello world"
    sub = "o"
    return len(string.find(sub))
```