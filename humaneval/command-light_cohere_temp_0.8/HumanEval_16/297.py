```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test suite
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abcXyz') == 3
assert count_distinct_characters('jerry') == 4

# Main code
test_count_distinct_characters()
print("All tests passed!")
```