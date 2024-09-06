```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.value = len(characters))
    return characters.size()
```python
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XyXzYX') == 3
    assert count_distinct_characters(' jerry ') == 4
    assert count_distinct_characters('  123 456 ') == 6
    assert count_distinct_characters('123 xyzpy') == 4
```