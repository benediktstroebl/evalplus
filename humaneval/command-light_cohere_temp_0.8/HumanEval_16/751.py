```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    Args: 
        string (str): The input string
    Returns: 
        int: Number of distinct characters
    """
    import re
    string_chars = re.findall('[ compiling set from string  )
    return len(string_chars)

# Example function test
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3 # Should be 3
    assert count_distinct_characters('Jerry') == 4 # Should be 4
test_count_distinct_characters()
```