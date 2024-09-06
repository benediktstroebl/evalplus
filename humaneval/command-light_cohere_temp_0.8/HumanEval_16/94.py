```python
def count_distinct_characters(string: str):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    Args: 
        string (str): input string
    Returns: 
        int: number of distinct characters
    """
    return len(set(string.strip()))

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('ABC123') == 5
    assert count_distinct_characters('Xyz123') == 5
    assert count_distinct_characters('gErry') == 3
```