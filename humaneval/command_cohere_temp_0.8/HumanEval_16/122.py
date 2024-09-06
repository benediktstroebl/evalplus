Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to handle the distinct characters in the given string regardless of case. The `lower()` method is applied to convert all characters in the string to lowercase before counting. Thus, it returns the correct number of distinct characters.