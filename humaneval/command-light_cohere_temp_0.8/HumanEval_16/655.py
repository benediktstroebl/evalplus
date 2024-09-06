```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('abcX') == 3
    assert count_distinct_characters('ABC') == 2
    assert count_distinct_characters('') == 0
```