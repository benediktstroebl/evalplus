```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string regardless of case.
    Args: string (str): str (input)

    Returns: int (number of distinct characters)
    """
    import string
    characters = set(string)
    return len(characters)

# Test the function
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters(' Jerry') == 4
    assert count_distinct_characters('abcABC123') == 5
    assert count_distinct_characters('A 23') == 4
```