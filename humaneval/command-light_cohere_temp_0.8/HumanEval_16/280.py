```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()}
 _not in string.
    return 0
```
def test_count_distinct_characters():
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('XyX') == 2
    assert count_distinct_characters('jerry') == 4
    assert count_distinct_characters('  jerry  ') == 4
    assert count_distinct_characters('  ABCDEFGHIJKLMNOPQRSTUV') == 21
```
The `count_distinct_characters` function returns the number of distinct characters in the given string. The `test_count_distinct_characters` function contains several test cases that validate the functionality of the `count_distinct_characters` function with various input strings.