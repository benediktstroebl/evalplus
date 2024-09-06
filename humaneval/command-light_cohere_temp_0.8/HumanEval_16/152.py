```python
def count_distinct_characters(string):
    """
    Return the count of distinct characters in the given string, regardless of case.
    """
    return len(set(char for char in string.lower()))
```

Here's a function that calculates the number of unique characters in a given string, regardless of case.