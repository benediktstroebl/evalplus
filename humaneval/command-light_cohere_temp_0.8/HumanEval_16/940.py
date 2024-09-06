```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.
    if c not in 'abcdefghijklmnopqr'})

# Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('Jerry'), 4)
assertEqual(count_distinct_characters('A'), 5)
assertEqual(count_distinct_characters('ZYX'), 4)
assertEqual(count_distinct_characters('').join(str.count_distinct_characters(' Jerry XYZ ')), 6)
```