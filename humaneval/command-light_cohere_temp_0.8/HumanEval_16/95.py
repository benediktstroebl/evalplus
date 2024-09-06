Here's a self-contained Python function that counts the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.vector() if c not string.count(c)})
```

This function utilizes a generator expression along with the `count()` function to determine the distinct character count in the provided string. It then returns the value, which corresponds to the count of distinct characters.

This function is completely self-contained and doesn't rely on any external variables or functions.