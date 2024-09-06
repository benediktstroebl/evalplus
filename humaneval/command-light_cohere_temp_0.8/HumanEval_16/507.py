```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
# Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('jerry'), 4)
```