```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.casefold})
IF(string == '', [])
    return 0

#Tests
def test_count_distinct_characters():
    assert count_distinct_characters('') == 0

def test_count_distinct_characters_valid():
    assert count_distinct_characters('xyzXYZ') == 3
def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters('jerry') == 4
```