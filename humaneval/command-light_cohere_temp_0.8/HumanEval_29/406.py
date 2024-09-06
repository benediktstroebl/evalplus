Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. The function utilizes the `startswith` method to filter the strings.