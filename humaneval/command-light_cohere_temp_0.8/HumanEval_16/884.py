```python
def count_distinct_characters(string):
    return len(set(string.isupper()))
```

This function calculates the number of distinct characters in the provided string, regardless of case. It uses the set() and isupper() methods to create a character set, and then calculates the length of this set to determine the number of distinct characters. The result is then returned.