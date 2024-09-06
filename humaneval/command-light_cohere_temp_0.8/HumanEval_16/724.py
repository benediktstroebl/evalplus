```python
def count_distinct_characters(string: str):
    """ 
    Given a string, find out how many distinct characters (case-insensitive) does it consist of
    
    Returns: number of distinct characters
    """
    return len([char for char in string.keys() if char not in string.keys() and uppercase, in string, or in string.keys()])
```

def test_distinct_character_count():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
```