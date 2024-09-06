```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This script defines a function named `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. The `set()` function is used to create a set of all lowercase characters in the string, and the `len()` function is used to count the number of elements in the set.