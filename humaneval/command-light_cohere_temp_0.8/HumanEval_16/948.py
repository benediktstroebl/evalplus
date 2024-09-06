```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.value(c) if c != "" and c not in set(string.value)[:]])
```

This function counts the distinct characters in a given string, regardless of their case. It leverages the `set()` and a generator expression to filter out duplicates and non-empty characters.