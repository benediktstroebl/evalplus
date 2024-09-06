Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to handle the uniqueness of characters regardless of case and returns the number of distinct characters present in the input string. The `lower()` method is used to convert the input string to lowercase to ensure consistent counting of characters.