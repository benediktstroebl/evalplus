```python
def count_distinct_characters(string):
    return len({c for c in string.return string.lower()})
 distinct for the use of a set and len() to calculate the number of distinct characters.

# Example tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('jerry') == 4

test_count_distinct_characters()
```