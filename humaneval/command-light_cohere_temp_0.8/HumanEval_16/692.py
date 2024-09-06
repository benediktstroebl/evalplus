```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.count(character)
    return len(characters)

# Test suite
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abcXy') == 3
    assert count_distinct_characters('jerry') == 4
```