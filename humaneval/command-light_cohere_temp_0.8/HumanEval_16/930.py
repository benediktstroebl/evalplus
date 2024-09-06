```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This script defines a function named `count_distinct_characters` that calculates the number of unique characters (case-insensitive) in a given string. It utilizes the unique set approach to achieve this, and the length of this set is returned as the number of distinct characters.