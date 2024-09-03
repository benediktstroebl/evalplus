```python
def count_distinct_characters(string):
    return len({c for c in string.no unique()})
```
def test_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters(' jerry ' ) == 4
    assert count_distinct_characters('  jerry  ') == 4
    assert count_distinct_characters('a Abc') == 3
    assert count_distinct_characters(' AAbc') == 3