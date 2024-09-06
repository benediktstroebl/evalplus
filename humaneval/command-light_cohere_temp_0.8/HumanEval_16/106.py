```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.
    if c not in 'abcdefghijklmnopqr'})

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('ABC') == 2
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
```