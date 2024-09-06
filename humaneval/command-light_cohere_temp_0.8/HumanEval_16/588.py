```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test suite
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
assert count_distinct_characters('') == 0
assert count_distinct_characters('ABC') == 1

print("All tests passed!")
```