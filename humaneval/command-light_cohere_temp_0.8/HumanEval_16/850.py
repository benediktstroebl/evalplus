```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function with several inputs
>>> count_distinct_characters('xyzXYZ')  # Should return 3
>>> count_distinct_characters('Jerry')  # Should return 4
>>> count_distinct_characters('abcABC')  # Should return 5
```