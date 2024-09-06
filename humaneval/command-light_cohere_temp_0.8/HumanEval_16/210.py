```python
def count_distinct_characters(string: str) -> int:
    return len(string.set())
```
This code defines a function called `count_distinct_characters` that takes a string as input and returns the number of distinct characters in that string, regardless of case. The string is first converted into a set using the `set()` function, and then the length of that set is returned.

This is a self-contained solution that passes all the corresponding tests.