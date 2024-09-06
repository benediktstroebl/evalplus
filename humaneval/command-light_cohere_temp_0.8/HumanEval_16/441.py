```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
```
# Unit tests
def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('def') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('  jerry   ') == 4
    assert count_distinct_characters('abc123') == 3
    assert count_distinct_characters('XYZ123') == 3
```