```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string Count overlaping cases."""
    return sum(1 for _ in string.find(substring, string))
```