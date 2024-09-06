Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to calculate the distinct characters in the provided string, regardless of case, and then returns the length of this set, which is the desired count. The `lower()` method is applied to ensure case insensitivity.