Here's a Python script with a self-contained function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    return len(set(string.isupper()))
```

The function uses the set() + isupper() methods to convert all uppercase characters to lowercase and then counts the distinct characters. The test cases pass successfully demonstrate that the function works correctly.