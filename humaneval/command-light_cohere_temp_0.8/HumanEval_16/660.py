Here's a self-contained Python script that defines a function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not set()})
```

This function utilizes a generator expression and the `len` function to calculate the number of unique characters in the input string, regardless of case sensitivity. The function can be easily tested by passing different strings to ensure it's functionality correctly.