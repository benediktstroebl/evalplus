```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This function uses the `find()` method to search for the given substring in the original string. The function returns the the number of times the substring appears in the string, not counting overlapping matches.