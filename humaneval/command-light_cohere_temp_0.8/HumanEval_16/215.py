```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.isalpha() and distinct() for c in string})

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Foobar') == 4
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters(' jerry ) == 4
    assert count_distinct_characters(' j R  \ n erry') == 4
    assert count_distinct_characters('   jerry  ') == 4
```