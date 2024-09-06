Here's a self-contained Python function that solves the problem of counting the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isalpha()}  #
```

This function leverages the `isalpha()` method of each character in the string, which returns `True` if the character is a letter (either lowercase or uppercase), and returns `False` otherwise. The function then returns the  the length of the resulting set, which contains only distinct characters, giving us the count of distinct characters in the original string.