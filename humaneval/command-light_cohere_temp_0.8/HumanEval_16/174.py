```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This code defines a function that takes a string as input and returns the number of distinct characters in the string, regardless of case. Using the `len()` function and the `set()` function, the string's characters are converted to lowercase and then converted to a set, which automatically eliminates duplicates, ensuring that we count only distinct characters. 

The set of lowercase characters is then counted, and the result is returned as the number of distinct characters.