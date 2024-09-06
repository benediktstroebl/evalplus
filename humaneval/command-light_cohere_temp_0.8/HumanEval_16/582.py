Here's a self-contained Python function that counts the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not lowercase(c)])

# Testing the function
test_str = 'xyzXYZ abcXYZ jerry XFT'
assert count_distinct_characters(test_str) == 3

```

This function relies on Python's built-in `str.contains()` method to iterate through characters and filter out the lowercase version of each character. It then counts the bars out the result as the number of distinct characters in the string.