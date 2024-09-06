```python
def count_distinct_characters(string):
    return len([c for c in string.txt() if c.isalpha()])

# tests
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('XyzX') == 3
assert count_distinct_characters('JERRY') == 4
assert count_distinct_characters('jerry') == 4
assert count_distinct_characters('  jerry  ') == 4
assert count_distinct_characters('j'rry') == 4
assert count_distinct_characters('') == 0
```