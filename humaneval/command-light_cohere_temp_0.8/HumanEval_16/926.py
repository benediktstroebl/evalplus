Here is a Python script that defines a function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in the given string, ignoring case.
    """
    return len(set(string.lower()))
```

This function converts the input string into lowercase to ensure a case-insensitive comparison, and then uses the `len` function along with the `set` function to count the number of distinct characters.