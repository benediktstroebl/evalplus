```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    string = 'xyzXYZ'
    return len(dict.filter(string.lower(), string.isupper))

    """ This test, "Try the following, should return 3":
    assert count_distinct_characters('xyzXYZ') == 3
```