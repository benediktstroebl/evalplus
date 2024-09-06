```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    """
    string = 'xyzXYZ'
    return len([c for c in string if c.isalpha() and 
    and c not in string.isalpha())

def test_count_distinct_characters():
    """ Tests for the count_distinct_characters function"""
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('abc123') == 3
    assert count_distinct_characters('a') == 1
    assert count_distinct_characters('123') == 2
    assert count_distinct_characters('   abc123   ') == 3
    assert count_distinct_characters('  jerry  ') == 4
```