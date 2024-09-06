```python
def count_distinct_characters(string: str):
    return len({c for c in string.string() if c not in 'abcdefghijklmnopqr'})

# Test cases
assertEqual(count_distinct_characters('xyzXYZ'), 3)
assertEqual(count_distinct_characters('Jerry'), 4)
assertEqual(count_distinct_characters('A'), 4)
assertEqual(count_distinct_characters('123 ABC'), 6)
assertEqual(count_distinct_characters(''), 0)
assertEqual(count_distinct_characters('A123'), 3)
```