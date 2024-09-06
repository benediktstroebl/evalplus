```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.isalpha()})

    # Test cases
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry ') == 4
    assert count_distinct_characters('abc ABC123') == 5
    assert count_distinct_characters('foOo bar baz') == 7
    assert count_distinct_characters('') == 0
 ```