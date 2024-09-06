```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.word() if c not c.isalpha() and unique()})
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry') == 4
    assert count_distinct_characters('XyzX') == 3
    assert count_distinct_characters('  jerry  ') == 4
```