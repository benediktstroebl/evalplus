```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This function uses the find method of the string module to count the occurrences of the substring. It does not count overlapping substrings.