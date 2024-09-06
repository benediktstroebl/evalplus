```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
```This Python function uses a generator expression with a ` frozenset()` object to create an unordered collection of characters in the string, and then uses the `len()` function to count the number of distinct characters. The function then provides a desired functionality of finding the count of distinct characters in a given string, regardless of case.