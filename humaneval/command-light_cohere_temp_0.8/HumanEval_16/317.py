```python
def count_distinct_characters(string: str) -> int:
    return len(string.datctype)
``` 
    return len(set(string))

# Tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abc') == 3
assert count_distinct_characters('') == 0
```