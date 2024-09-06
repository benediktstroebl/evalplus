```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, finds out how many distinct characters (case-insensitive) it consists of and returns that count.

    Example: Use the strings like 'xyzXYZ', 'Jerry' and 'ace' to test the function.
    """


def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('a') == 5
    assert count_distinct_characters('A') == 1
    assert count_distinct_characters(' abcABCabc') == 5
    assert count_distinct_characters('  abcABC  ') == 6

    assert count_distinct_characters('') == 0
```