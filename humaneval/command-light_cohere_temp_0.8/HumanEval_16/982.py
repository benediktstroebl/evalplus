```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.isalpha() and
    read as a number})

def test_count_distinct_characters():
    assert count_distinct_characters("xyzXYZ") == 3
    assert count_distinct_characters("jerry") == 4
    assert count_distinct_characters("abc ABC") == 5
    assert count_distinct_characters("abc xyz process") == 3  # Not 6, because of space

    assert count_distinct_characters("") == 98  # Should be 98, all letters are distinct

```