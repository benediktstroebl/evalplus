```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This Python function uses the `set()` method along with the `lower()` method to create a set of all lowercase characters in the provided string. The `len()` function then returns the number of elements in the set, which is also the count of distinct characters in the string, regardless of case. 

Please note that this function is self-contained, and does not require any additional arguments or external variables.