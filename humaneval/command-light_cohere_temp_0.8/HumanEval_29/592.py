Here's a self-contained Python function that filters strings by their prefix:
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses the starts-with operator to filter out strings that do not start with the given prefix.