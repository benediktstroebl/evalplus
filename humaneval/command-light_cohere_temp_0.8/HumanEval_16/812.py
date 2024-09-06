```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not string.isalpha(c)})
```

This code defines a function that calculates the number of distinct characters in a given string. It uses a classic set-based approach with a generator expression to filter out non-alphanumeric characters and then counts the remaining unique characters. The result is a straightforward extension of the string's character count without the need for explicit character comparison.