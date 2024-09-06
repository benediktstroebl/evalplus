Here's a Python script with a self-contained function that counts the number of distinct characters in a given string:
```python
def count_distinct_characters(string):
    return len({c for c in string.unique.lower() if c in string})
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the count of distinct characters in the string, regardless of case. The function uses a `lower()` method to convert all characters to lowercase before performing a set operation to count distinct characters.