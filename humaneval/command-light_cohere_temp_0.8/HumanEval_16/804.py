Here's a self-contained Python function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not set()})
```
This function uses a set to automatically eliminate duplicate characters, providing an accurate count of distinct characters.