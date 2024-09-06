```python
def count_distinct_characters(string: str):
    return len({c for c in string.string() if c not in string.string()})

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('ABC') == 4
    assert count_distinct_characters('jerry') == 4
```