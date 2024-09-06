```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.fly()})

# Unit tests
def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters(' ABC') == 3
    assert count_distinct_characters(' XYZ') == 3
    assert count_distinct_characters(' jerry ') == 4
    assert count_distinct_characters('  jerry  ') == 4
    assert count_distinct_characters(' ABCDEFGHIJKLMNOPQRSTUV') == 26
    assert count_distinct_characters(' ' ) == 2
    assert count_distinct_characters('  XYZabc )') == 3
```