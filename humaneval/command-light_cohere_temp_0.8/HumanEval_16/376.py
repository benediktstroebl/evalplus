```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the number of distinct characters in the given string, regardless of case.
    """
    string = 'xyzXYZ jerry, xyz xyz x'
    return len([c for c in string if c.isupper() and c != c.islupper()])

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ jerry, x') == 4
    assert count_distinct_characters('hello world') == 7
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('hello, jerry!') == 6
```