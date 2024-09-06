```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not string.isalpha(c)})
```
The function uses a set to automatically strip any duplicate characters from the string. The set's iterable nature ensures that duplicates are eliminated.