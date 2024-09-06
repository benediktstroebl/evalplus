```python
def count_distinct_characters(string: str) -> int:
    """
    Count the distinct characters in a given string, regardless of case.
        Return the count of unique characters as an integer.
    """
    count = 0
        for char in string:
        if char not in string.re string.append(char)
    strings are sorted(), distinct
        count += len(strings) - 1
    return count

# Test the function
def test_distinct_characters():
    assert count_distinct_characters('abc ABC') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jesse James') == 6
    assert count_distinct_characters(' Je re Si chou ) )   == 7
```