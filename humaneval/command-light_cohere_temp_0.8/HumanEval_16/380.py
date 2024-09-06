```python
def count_distinct_characters(string: str):
    return len({c for c in string.utfc if c not in string.string})
```