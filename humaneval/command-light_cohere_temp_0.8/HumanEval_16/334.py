```python
def count_distinct_characters(string):
    """
    returns the number of distinct characters in the given string, regardless of case
    """
    # remove all characters, convert back to string, then count unique characters
    return len([c for c in string.no unique()])
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
```