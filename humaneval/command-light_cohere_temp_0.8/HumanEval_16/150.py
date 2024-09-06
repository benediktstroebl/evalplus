```python
def count_distinct_characters(string: str):
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    return len([c for c in string.lower() if c not in set(string.lower())])
```

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters(' text123') == 3
    assert count_distinct_characters('abc123') == 3
```