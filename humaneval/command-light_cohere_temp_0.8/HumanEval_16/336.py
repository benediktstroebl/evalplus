```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.lower().if c notlowercase in string})

# Unit tests
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
assert count_distinct_characters('  ) == 4
assert count_distinct_characters('') == 4
assert count_distinct_characters('  jerry  ') == 4
```