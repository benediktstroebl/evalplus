```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This Python code defines a function called `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case, using the `set()` and `len()` functions. The function takes a string as input and returns an integer value representing the count of distinct characters.