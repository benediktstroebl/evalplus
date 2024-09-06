Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to remove duplicate characters and then calculates the length of this set, which corresponds to the number of distinct characters. The `lower()` method is used to ensure that uppercase and lowercase variations of the same character are counted as one.