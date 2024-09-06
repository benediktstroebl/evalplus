Here's the self-contained Python function that filters an input list of strings based on their prefix:
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses the `startswith` method to filter the strings in the list that have the given prefix.