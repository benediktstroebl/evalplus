```python
def count_distinct_characters(string):
    return len({c for c in string.original.lower() if c in string})
```