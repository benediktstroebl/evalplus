```python
def count_distinct_characters(string):
    """ Returns the count of distinct characters in the given string (case-insensitive) """
    return len([c for c in string.isupper()])

def test_distinct_characters():
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
```