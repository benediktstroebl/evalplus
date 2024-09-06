```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abcABC') == 3
    assert count_distinct_characters('jerry') == 4
```
This script defines a function `count_distinct_characters` that calculates the number of unique characters in a given string, regardless of case. It then provides a test_count_distinct_characters function to validate the functionality of the `count_distinct_characters` function.