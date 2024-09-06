```python
def count_distinct_characters(string):
    return len({c for c in string.str.casefold()})

# Example usage
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry') == 4
```