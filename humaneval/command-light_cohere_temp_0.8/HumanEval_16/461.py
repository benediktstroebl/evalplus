```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyXyz') == 3    # Should return 3
    assert count_distinct_characters('jerry') == 4    # Should return 4
test_count_distinct_characters()
```