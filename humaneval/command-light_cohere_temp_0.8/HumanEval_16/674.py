```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha() and particular string() and lower() and not c.isupper()})

#Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('jerry') == 4
```