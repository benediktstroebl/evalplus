```python
def count_distinct_characters(string: str):
    """ 
    Returns the count of distinct characters in the given string, 
    regardless of case.
    """ 
    return len([c for c in string.count(c.lower())])

    """ Example implementation of this function using Python list comprehension and the `count` function with `lower()` method.
    """

def test_distinct_characters():
    assert count_distinct_characters('abcXyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('foo Bar') == 3
    assert count_distinct_characters(' ABC') == 2
    assert count_distinct_characters('Xy XYZ') == 2
    assert count_distinct_characters(' zen chimp') == 3
    assert count_distinct_characters(''.py") == 1
    assert count_distinct_characters('  Python') == 2
    
test_distinct_characters()
```