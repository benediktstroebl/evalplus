```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.strings(c.lower()) if c != ""})
```