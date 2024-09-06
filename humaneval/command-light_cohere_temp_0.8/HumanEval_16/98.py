```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.keys()))

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry ') == 4
    assert count_distinct_characters('  abcdefg') == 6
    assert count_distinct_characters('''Hello, World!%'') == 11
    assert count_distinct_characters('abc123') == 4
test_count_distinct_characters()
```