```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.ct.count(c,case(string))})

# Basic tests
test_count_distinct_characters = """
def test_count_distinct_characters():
    assert count_distinct_characters("abc") == 3
assert count_distinct_characters("XyzXYZ") == 3
assert count_distinct_characters("jerry") == 4
assert count_distinct_characters("") == 0
"""

# Run the tests when you've defined the function
```