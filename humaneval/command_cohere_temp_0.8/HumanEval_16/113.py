Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to count the distinct characters in the provided string, regardless of case. The `lower()` method is applied to convert all characters in the string to lowercase before counting. The `len()` method then returns the size of the set, which is the number of distinct characters.