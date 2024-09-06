```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    """
    string = str(string)
    substring = str(substring)
    return _how_many_times(string, substring)

def _how_many_times(string, substring):
    return (len(string) == 0) ? 0 : sum(1 for m in string if m == substring)
```