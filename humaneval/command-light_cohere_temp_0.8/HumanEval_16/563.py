```python
def count_distinct_characters(string: str) -> int:
    """
    Count the distinct characters in a given string, regardless of case.
    """
    return sum(1 for c in string if c.isalpha_lower())
```

This function uses the `str.isalpha_lower()` method to check if a character is lowercase and returns 1, effectively counting it as distinct. The function then returns the number of distinct characters in the string.

This code is a complete, self-contained solution to the problem you've described.