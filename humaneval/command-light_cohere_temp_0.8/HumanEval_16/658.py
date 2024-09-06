```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, regardless of case.
    """
    return len({c for c in string.lower() if c not in string.lower()})

    tests:
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry') == 4
    assert count_distinct_characters('JER') == 4
    assert count_distinct_characters('J') == 4
    assert count_distinct_characters('') == 0
    assert count_distinct_characters('123') == 2
    assert count_distinct_characters('abcABC') == 3
```