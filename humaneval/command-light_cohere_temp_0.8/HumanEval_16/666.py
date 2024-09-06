Here is a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isupper() and is distinct})

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XYZ') == 3
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('abcABC') == 3
    assert count_distinct_characters('ayer') == 2
```
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, and then provides unit tests to verify its correctness.  The outputs should correspond to the expected results.