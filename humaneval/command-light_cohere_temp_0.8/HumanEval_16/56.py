```python
def count_distinct_characters(string: str):
    return len({c for c in string.cd distinct(c) for c in string})

# Test suite
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('Jerry') == 4
```