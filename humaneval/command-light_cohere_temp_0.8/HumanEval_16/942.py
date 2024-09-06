```python
def count_distinct_characters(string: str):
    return len({c for c in string.getc() if c not in set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}

# Test case 1
assert count_distinct_characters('xyzXYZ') == 3

# Test case 2
assert count_distinct_characters('Jerry') == 4
```