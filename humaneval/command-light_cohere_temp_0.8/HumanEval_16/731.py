```python
def count_distinct_characters(string):
    return len({c for c in string.str(lowercase()) if c not in string.str(uppercase()).ess})

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
assert count_distinct_characters('1234') == 4
assert count_distinct_characters('jerry1234') == 5
assert count_distinct_characters(' writing a book') == 7
```