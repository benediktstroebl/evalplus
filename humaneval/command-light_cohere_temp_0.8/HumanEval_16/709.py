Here is a Python script that contains a self-contained function to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in the given string, regardless of case.
    """
    return len([c for c in string if c.isalpha()))
```
def test_distinct_character_count():
    """
    Test the count_distinct_characters function
    """
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('Hello World!!') == 7
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('ABC') == 3
```