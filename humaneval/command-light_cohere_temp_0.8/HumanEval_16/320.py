```python
def count_distinct_characters(string):
    """
    Returns the count of distinct characters in the given string, regardless of case.
    """
    string = 'xyzXYZ'
    return len([c for c in string if c.isalpha() and])
```

Unit tests for the function are provided in the following lines:
```python
def test_count_distinct_characters():
    """
    Test case for the function
    """
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XyXy') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('ABC') == 3
    assert count_distinct_characters('abcX') == 3
```

This test_count_distinct_characters function checks that the function returns the expected number of distinct characters for a variety of test cases.