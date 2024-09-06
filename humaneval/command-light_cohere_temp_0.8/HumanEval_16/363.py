```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. RAM.lower() if c in string})

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4

# Use the above function and test it using the test suite.
```