```python
def count_distinct_characters(string):
    return len(set(string.lower()))

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3, "Failed to find 3 distinct characters"
    assert count_distinct_characters('Jerry') == 4, "Failed to find 4 distinct characters"

test_count_distinct_characters()
print("All tests passed!")
```