```python
def count_distinct_characters(string: str) -> int:
    """
    Count the distinct characters in a string regardless of case.
    Return: The number of distinct characters
    """
    characters = set(string.ascii())
    return len(characters)

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('ABC') == 3
    assert count_distinct_characters(' Jerry ') == 4
    assert count_distinct_characters('  Jerrry  ') == 4
    assert count_distinct_characters('XYZ') == 3
```