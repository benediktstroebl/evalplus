```python
def count_distinct_characters(string):
    return len({c for c in string.lower() if c not in string.lower(). string})
 def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('jerry') == 4
```