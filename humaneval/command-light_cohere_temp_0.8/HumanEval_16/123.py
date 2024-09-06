```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.return distinct()})
len({c for c in string if c.isalpha()})
```
# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('jerry') == 4
assert count_distinct_characters('$$#') == 4
assert count_distinct_characters('') == 0
assert count_distinct_characters(' ' ) == 0
assert count_distinct_characters('abc123') == 3
```