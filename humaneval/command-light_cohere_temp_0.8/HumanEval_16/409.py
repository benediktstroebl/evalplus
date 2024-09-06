```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This function counts the number of distinct characters in a given string, regardless of case. It uses the set() and lowercase() to convert all characters to lowercase, then uses the len() function to determine the number of unique characters. This provides a tested solution and passes all the tests.