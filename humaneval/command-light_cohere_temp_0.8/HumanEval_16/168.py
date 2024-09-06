Here is a Python script with a self-contained function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not str.lowercase() and string})
```

This function uses a set to remove duplicate characters and counts the unique characters. The `len()` function then returns the number of unique characters in the string.