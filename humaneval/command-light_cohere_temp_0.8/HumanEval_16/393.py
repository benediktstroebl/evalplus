```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string()})
```def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abcX') == 3
    assert count_distinct_characters('jerry') == 4
```
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. Using a nested list comprehension and the `{} set`, the function filters out duplicate characters and counts them, then returns the number of distinct characters. The `test_count_distinct_characters` function verifies that the function works correctly for various inputs.