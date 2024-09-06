```python
def count_distinct_characters(string):
    return len([c for c in string.no unique()])
```
# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('jerry') == 4
assert count_distinct_characters(' ') == 0
assert count_distinct_characters('A') == 1
assert count_distinct_characters('Test') == 8
```