```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This code defines a function named `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case, using the `set()` and `len()` functions. The test cases are also provided to ensure that the function works correctly for all input strings.