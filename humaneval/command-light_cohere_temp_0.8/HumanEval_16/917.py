```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c not in 'abcdefghijklmnopqr'})

# Unit tests
test_count_distinct_characters = lambda: assert count_distinct_characters('xyzXYZ') == 3
test_count_distinct_characters('Jerry') == 4
```