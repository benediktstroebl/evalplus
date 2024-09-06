```python
def count_distinct_characters(string):
    return len([c for c in string.get(str, ""). call_count: len(c) > 1 for c in string])

# Test the function
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
```