Here's a self-contained Python function that finds the number of times a given substring can be found in the original string, while accounting for overlapping occurrences:
```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring, string))
```

This function uses the `find()` method to search for the given substring in the original string. The length of the string is then returned.