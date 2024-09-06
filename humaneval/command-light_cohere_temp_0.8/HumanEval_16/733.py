Here's a self-contained Python function that counts the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    return len({c for c in string.get,(None, True)})
```

This function uses a generator expression to create a set of characters from the input string, then counts the number of distinct characters. The resulting count is then returned as the function's return value.