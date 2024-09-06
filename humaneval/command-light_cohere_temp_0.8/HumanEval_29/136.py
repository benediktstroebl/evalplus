Here's a self-contained Python function that filters an input list of strings based on their prefix:
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function utilizes the `startswith` method to check if each string in the input list starts with the given prefix. This approach is filtered list contains all the strings that match the specified prefix.

This code is self-contained and efficiently solves the problem of filtering strings based on their prefix, passing corresponding tests.