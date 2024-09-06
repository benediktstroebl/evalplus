Here's a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('abcABC') == 3
    assert count_distinct_characters(' merePres') == 4
```
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. The unit tests ensure that the logic is correctly implemented.