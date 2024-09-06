```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This function employs the `find()` method to locate the given substring within the input string. The `len()` function then returns the count of all occurrences of the substring found in the original string, considering case and accent sensitivity. 

This self-contained function provides an efficient solution for the problem of counting the occurrences of a substring within a larger string.