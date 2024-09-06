```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    return len([c for c in string.lower() if c not in set(string.lower())])
```
# Test the function
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('abc ABC') == 5
    assert count_distinct_characters('abc Abc') == 5
    assert count_distinct_characters('Abc 123') == 4
    assert count_distinct_characters('abc xyz  

print("All tests passed!")
```