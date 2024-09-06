```python
def count_distinct_characters(string):
    """ 
    Returns the count of distinct characters in the string, 
    regardless of case.
    """
    string = 'xyzXYZ'
    return len([c for c in string if c.isupper() and is not in string.isupper()])
 def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('XyzX') == 3
    assert count_distinct_characters('foo bar') == 5
    assert count_distinct_characters('JERRY') == 4
```