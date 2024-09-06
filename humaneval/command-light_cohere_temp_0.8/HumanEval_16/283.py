Here's the code that addresses your problem, which aims to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This script defines a function `count_distinct_characters` that takes a string as input and employs the `set()` and `lower()` methods to eliminate duplicates and convert all characters to lowercase. The `len()` function then calculates the count of unique characters, resulting in the total number of distinct characters in the string.

You can utilize this function to determine the count of distinct characters for any given string.