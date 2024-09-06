```python
def count_distinct_characters(string):
    return len([c for c in string.no pure_lowercase(c) for c in string])

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('').count() == 0
```