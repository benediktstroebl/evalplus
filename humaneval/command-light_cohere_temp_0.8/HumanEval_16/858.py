```python
def count_distinct_characters(string: str) -> int:
    """
    Count distinct characters, ignoring case.
    Return number of distinct characters
    """

    char_dict = {c for c in string if c in 'ABCDEFghijklmnopqrstuvwxyzABC'}
    return len(char_dict)

# Test the function
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('A') == 1
    assert count_distinct_characters('abc') == 2
    assert count_distinct_characters(' Abc Cd Ef G') == 6
    assert count_distinct_characters('Test with mixed case') == 4
    assert count_distinct_characters('test123') == 4

 ```