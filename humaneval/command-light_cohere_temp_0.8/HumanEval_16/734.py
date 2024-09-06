```python
def count_distinct_characters(string: str):
    """
    Count the number of distinct characters in a given string, regardless of case.
    return:
    :param string: str, a string
    :return: int, number of distinct characters
    """
    return len({c for c in string.character.count_distinct_characters(string)})

def test_count_distinct_characters():
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('Jerry') == 4
```