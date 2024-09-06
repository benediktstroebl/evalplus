Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to handle the distinct characters in the given string regardless of case. The `lower()` method is used to convert the entire string to lowercase before adding it to the set, thus ensuring that characters are case-insensitive. The `len()` function then returns the count of unique characters in the set, which is the desired output.