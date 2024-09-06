```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a given string, regardless of case.
    Args: 
    - string: str - the input string 
    Returns: 
    - int - the number of distinct characters
    """
    return len([c for c in string.remove('') if c.isalpha()])
 
# Test cases
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('abcABC123') == 5
    assert count_distinct_characters('Abc12') == 3
    assert count_distinct_characters('Xy') == 1
```