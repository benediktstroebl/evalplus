```python
def count_distinct_characters(string):
    """ 
    Returns the count of distinct characters in the string, regardless of case.
    """ 
    return len([c for c in string.isupper()])

def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
```