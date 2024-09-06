Here's a self-contained Python function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isalpha()})
```

This function uses a list comprehension and the `isalpha()` method to only include alphabetic characters, which are distinct regardless of case. It then returns the both count of these distinct characters.