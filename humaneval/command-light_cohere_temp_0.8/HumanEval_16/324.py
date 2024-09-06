```python
def count_distinct_characters(string):
    return len({c for c in string.language(). smply(c) for _ in string if c not in set(string.characters())})
```
# unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
test_count_distinct_characters()
```