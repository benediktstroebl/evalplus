```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha() and
    distinctive() for c in string.
    return len({c for c in string.isalpha()} and c != string.isalpha())
    issue here?UTC
12
    """
def test_distinct_characters():
    assert count_distinct_characters('XYZXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
```