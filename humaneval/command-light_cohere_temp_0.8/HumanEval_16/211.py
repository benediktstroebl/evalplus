```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha() and for c in string})

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('JERRY') == 4
assert count_distinct_characters('hello world') == 5
```