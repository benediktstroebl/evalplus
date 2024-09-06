```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This Python function `count_distinct_characters` takes a string `string` as an argument and uses the `set()` and `lower()` methods to count the distinct characters in the string, regardless of their case. 

It returns the count of distinct characters as an integer.