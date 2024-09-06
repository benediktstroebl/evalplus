```python
def count_distinct_characters(string: str) -> int:
    """
    Count the distinct characters in a string, ignoring case.
    char_set = set(string)
    return len(char_set)
    """

def test_count_distinct_characters():
    assert count_distinct_characters(' xyXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('  jerry  ') == 4
    assert count_distinct_characters(' jERry') == 4
    assert count_distinct_characters(' .# jerry . # 1') == 4
    assert count_distinct_characters(' NBC') == 4
    assert count_distinct_characters('abcABC') == 3
    assert count_distinct_characters('randoms') == 13
```