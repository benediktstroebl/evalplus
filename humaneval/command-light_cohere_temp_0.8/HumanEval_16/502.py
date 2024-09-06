```python
def count_distinct_characters(string):
    return len({c for c in string.upper() if c not in string.string()})

# unit tests
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
```