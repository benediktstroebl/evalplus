```python
def count_distinct_characters(string):
    return len({c for c in string.ref(lower=True) if c not in set(string.lower())})
```