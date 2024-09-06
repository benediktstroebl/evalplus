```python
def count_distinct_characters(string: str) -> int:
    """
        Count the distinct characters in a given string regardless of case
        :param string: str - input string 
        :return: int - number of distinct characters
    """
    characters = set(string.count(string))
    return len(characters)

# Tests
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XyX') == 2
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('  ) == 0
 ```