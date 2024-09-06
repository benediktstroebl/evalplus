```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()})

def test_distinct_character_count():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('test') == 5
    assert count_distinct_characters(' Jefferson') == 8
    assert count_distinct_characters('cB') == 6
    assert count_distinct_characters(' Abcdef ') == 5
```