```python
def count_distinct_characters(string: str):
    return len({c for c in string. characters() if c not string.isalpha(c)})
```