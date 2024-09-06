```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

The function uses the `find()` method to locate all occurrences of the substring within the original string. The `len()` function then returns the count of all occurrences, including the case of an empty string matching the substring.